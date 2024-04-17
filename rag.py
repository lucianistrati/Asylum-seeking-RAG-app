import os

import weaviate
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
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
from weaviate.embedded import EmbeddedOptions

folder_path = "data"
filepaths = [
    os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)
]
documents = []
for filepath in filepaths:
    loader = PyPDFLoader(filepath)
    documents.extend(loader.load())

embedding = OpenAIEmbeddings()

chunk_size = 200
chunk_overlap = 20


text_splitter = [
    CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap),
    RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap),
    SpacyTextSplitter(pipeline="de_core_news_sm"),
][-1]
print(text_splitter)

persist_directory = "embeddings/"


splits = text_splitter.split_documents(documents)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# retriever = FAISS.from_documents(documents,
#                                  embedding
#                                 #  OpenAIEmbeddings()
#                                  ).as_retriever()


retriever = vectorstore.as_retriever()  # chroma db used as retriever


model_name = "gpt-3.5-turbo"
temperature = 0
prompt = hub.pull("rlm/rag-prompt")
print("*prompt", prompt)
llm = ChatOpenAI(model_name=model_name, temperature=temperature)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# idea use those bge embedings, use mixtral too


# lastly fusion would be great to use

# hyde could also be used to generate a document and then embed it and then look for
# similarities within that genreated document and the other datapoints


#################

# this one extracts from each of the returned documents by the retriever and retrieve
# only relevant information

# making the compressor
# llm = OpenAI(temperature=0)
# compressor = LLMChainExtractor.from_llm(llm)
#
# # it needs a base retriever (we're using FAISS Retriever) and a compressor (Made above)
# compression_retriever = ContextualCompressionRetriever(
#     base_compressor=compressor, base_retriever=retriever
# )

################

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


# example_queries = [
#     "Wann darf jemand in privaten Wohnraum ziehen?",
#     "Hat man mit einer Duldung nach § 60a AufenthG Anspruch auf"
#     "Leistungen nach dem AsylbLG?",
#     "Was bedeutet rechtsmissbräuchliche Beeinflussung der"
#     "Aufenthaltsdauer i.S.d. § 2 AsylbLG?",
# ]
#
# k=3
#
# for query in example_queries[::-1]:
#     print("#" * 300)
#     print(rag_chain.invoke(query))
#     retrieved_docs = retriever.get_relevant_documents(
#         query,k=k
#     )
#     print(retrieved_docs)

irrelevant_questions = [
    "Wann überquerte George Washington den Delaware River?",
    "Wann wurde die Hamburger Asylbehörde gegründet?",
    "Was können Sie mir über die Verordnung Nr. 156/2023 sagen,"
    "die am 16. Dezember 2023 verabschiedet wurde?",
]
k = 3
for query in irrelevant_questions:
    if len(query) > 4096:
        query = query[:4000] + "\nAnswer:"
    retrieved_docs = retriever.get_relevant_documents(query, k=k)


def get_answer_and_sources(query):
    if len(query) > 4096:
        query = query[:4000] + "\nAnswer:"
    return rag_chain.invoke(query), retriever.get_relevant_documents(query, k=k)
