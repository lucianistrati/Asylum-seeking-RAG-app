# Onsite Day Task

It's great that you are joining us for an onsite day and we are really looking forward to it. Below, we have
specified an onsite day project for you to test your abilities and give you the opportunity to showcase what you can achieve.

You have time until the presentation for implementing it. Please don't hesitate to reach out in case you have any questions.

## Context

The purpose of Merantix Momentum is to implement machine learning solutions for clients with all sorts of use cases in all kinds of industries.

Your position is within the NLP team, implementing solutions that involve natural language.

## Project Specification

In this onsite day project, you are working to solve some issues the "Hamburger Asylbehörde" has. This public office is responsible for the asylum process in Hamburg, Germany. Employees of the office have to regularly respond to specific requests of asylees. Since legislation and other rules frequently change, this requires looking up relevant sources to determine how to respond to a specific request.

Your task is to build/design a tool that helps employees of the office to respond to requests. The tool should be able to retrieve relevant sources from the given data and formulate a response.

The folder `/data` contains relevant PDF files.

Example Questions are:

- Wann darf jemand in privaten Wohnraum ziehen?
- Hat man mit einer Duldung nach § 60a AufenthG Anspruch auf Leistungen nach dem AsylbLG?
- Was bedeutet rechtsmissbräuchliche Beeinflussung der Aufenthaltsdauer i.S.d. § 2 AsylbLG?

Be aware that your time is very limited. We know that you could spend days and weeks on this project. However, you only have ~5-6 hours.
So please prioritize and focus on the most important aspects. Don't worry if something doesn't work or you can only make a sketch. We will rate your work based on the decisions you made, on the code you wrote and on the creativity you showed.

### Tasks

1. Build a simple RAG pipeline to retrieve relevant sources from the given data and answer questions based on these sources. The deliverable should be a simple interface that allows to enter a question and returns a response. In a first iteration, you may choose to only have a command line interface.
2. Split the solution into components that can be reused and scaled independently. You could for instance have an API endpoint for the retriever.
3. Prepare to answer/present the following:
   - Does the solution have an interface? If not: what should it look like? If yes: how would you improve it? Make a rough sketch.
   - Describe how to evaluate the solution.
   - How should the solution be deployed?
   - Describe the future: What would you do next? What would you do if you had more time? What decisions have to be made?

## Deliverables

Please

1. Upload all code that pertains to your solution to this GitHub repository as a pull request **until end of the day**.

   Please write reusable, documented code.

2. Give a short presentation (around 20 minutes) in front of a small audience to summarize your work on the project.
   As stated earlier, you are free to choose the format of your presentation. You can use a slide deck, a demo, screensharing of code.
   Whatever you think is best to present your work.

Please communicate clearly any code in your solution that you didn’t write yourself.
