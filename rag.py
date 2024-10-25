import os
import weaviate
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    SpacyTextSplitter,
)
from langchain.vectorstores import FAISS, Chroma, Weaviate

# Define directory and load documents
folder_path = "data"
filepaths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]
documents = []
for filepath in filepaths:
    loader = PyPDFLoader(filepath)
    documents.extend(loader.load())

# Set embedding and text splitting configurations
embedding = OpenAIEmbeddings()
chunk_size = 200
chunk_overlap = 20

# Select a text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
print("Using Text Splitter:", text_splitter)

# Split documents and create a vector store
splits = text_splitter.split_documents(documents)
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding)
retriever = vectorstore.as_retriever()

# LLM and prompt configuration
model_name = "gpt-3.5-turbo"
temperature = 0
prompt = hub.pull("rlm/rag-prompt")
print("Using Prompt:", prompt)
llm = ChatOpenAI(model_name=model_name, temperature=temperature)

def format_docs(docs):
    """Formats a list of documents for readability."""
    return "\n\n".join(doc.page_content for doc in docs)

# RAG chain setup for retrieval and question-answering
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Example irrelevant queries
irrelevant_questions = [
    "Wann überquerte George Washington den Delaware River?",
    "Wann wurde die Hamburger Asylbehörde gegründet?",
    "Was können Sie mir über die Verordnung Nr. 156/2023 sagen, die am 16. Dezember 2023 verabschiedet wurde?",
]
k = 3
for query in irrelevant_questions:
    truncated_query = query[:4000] + "\nAnswer:" if len(query) > 4096 else query
    retrieved_docs = retriever.get_relevant_documents(truncated_query, k=k)

def get_answer_and_sources(query):
    """Fetches the answer and relevant documents for a given query."""
    truncated_query = query[:4000] + "\nAnswer:" if len(query) > 4096 else query
    return rag_chain.invoke(truncated_query), retriever.get_relevant_documents(truncated_query, k=k)
