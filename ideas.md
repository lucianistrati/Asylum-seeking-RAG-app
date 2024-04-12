documents sizes:

82 pages
1 page (the one with the branches)
24 pages
1 page (form)
79 pages

Mixtral handles 32k tokens - let's say 10k word - 20 pages

mistral7b -> mistral-tiny
mixtral8x7b -> mistral-small

unknown answers:
I'm sorry, but I don't have any information about
what the president said about Justice Breyer.

perhaps calculate similarity between the answer and the

"I'm sorry but I don't have
any information about"

or check that len(sources) is 0


irrelevant_questions = [
    "Wann überquerte George Washington den Delaware River?",
    "Wann wurde die Hamburger Asylbehörde gegründet?",
    "Was können Sie mir über die Hamburger Asylbehörde erzählen?"
    "Verordnung Nr. 124 am 15. Dezember 2023 verabschiedet?",
]

Evaluation criteria:

Information Retrieval Performance: if it qualitatively makes sense

Generation Quality: if it qualitatively makes sense

Integration of Retrieval and Generation:  if it qualitatively makes sense

Diversity of Responses: varying the temperature

User Satisfaction:  if it qualitatively makes sense

Training Data Quality: it is qualitative

Comparative Analysis: with and without rag

maybee create variations of that question and send in those questions too and then 
pick the best answer

or use a separate model to evaluate whether the context is relevant to the asked 
question 

what else to be done?

generate questions from already existing text and then answer them and expect the 
model to actually answer it and maybe to generate from one page and expect the answer 
to be asked from that same page and not from some other page

take random questions from the internet, possibly questions which are already of 
potential to cause hallucination, maybe dataset of hallucinative questions, 
nonsensical questions
