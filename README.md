# Asylum seeking RAG app

This projects aims to solve some of the issues that "Hamburger Asylbehörde" has. This public office is responsible for the asylum process in Hamburg, Germany. Employees of the office have to regularly respond to specific requests of asylees. Since legislation and other rules frequently change, this requires looking up relevant sources to determine how to respond to a specific request.

Your task is to build/design a tool that helps employees of the office to respond to requests. The tool should be able to retrieve relevant sources from the given data and formulate a response.

The folder `/data` contains relevant PDF files.

Example Questions are:

- Wann darf jemand in privaten Wohnraum ziehen?
- Hat man mit einer Duldung nach § 60a AufenthG Anspruch auf Leistungen nach dem AsylbLG?
- Was bedeutet rechtsmissbräuchliche Beeinflussung der Aufenthaltsdauer i.S.d. § 2 AsylbLG?

The solution that was developed comes with a streamlit developed chat app that uses langchain for the chat plugin that interacts with the Open AI API as well as the Mistral API (the choice of VectorDB for the project was PineconeDB).

pip install requirements.txt
