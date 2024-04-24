# Asylum Seeking RAG App

The Asylum Seeking RAG (Response Advisory Group) app aims to address some of the challenges faced by the "Hamburger Asylbehörde," the public office responsible for the asylum process in Hamburg, Germany. Employees of this office often need to respond to specific requests from asylum seekers, which may involve navigating complex legal and regulatory frameworks.

## Project Overview

The goal of this project is to develop a tool that assists employees of the office in responding to requests efficiently and accurately. The tool should be capable of retrieving relevant sources from provided data and formulating appropriate responses.

### Example Questions

Some example questions that the tool should be able to address include:

- When is someone allowed to move into private accommodation?
- Does someone with a tolerated stay (§ 60a AufenthG) have entitlement to benefits under the AsylbLG?
- What constitutes an abusive influence on the duration of stay according to § 2 AsylbLG?

## Solution Components

The solution developed for this project includes:

- **Streamlit Chat App**: A user-friendly interface developed using Streamlit, allowing users to interact with the tool via a chat-like interface.
- **Langchain Plugin**: Integration with Langchain for the chat plugin, facilitating interactions with the OpenAI API for natural language processing tasks.
- **Mistral API**: Integration with the Mistral API for additional functionality and data retrieval.
- **Vector Database**: The choice of VectorDB for the project was PineconeDB, providing efficient storage and retrieval of vector representations.

## Installation

To set up the project, run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## Source Files

The `src` directory contains the following Python files:

- `api.py`: Python file containing API functionalities.
- `mistral.py`: Python file containing functionalities related to the Mistral API.
- `rag.py`: Python file containing functionalities for the Response Advisory Group.

## Usage

Once the dependencies are installed, you can run the application by executing the appropriate command. Further instructions on how to use the application will be provided within the application interface.
