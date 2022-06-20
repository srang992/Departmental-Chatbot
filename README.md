
# Departmental Chatbot using Rasa NLU

In this project, I create a departmental chatbot using 
Rasa NLU. This robot can give answers to Department-related, 
and course-related queries of my college. The dialog part of 
this chatbot is programmed by myself. 

This repository contains all files related to this 
departmental chatbot. Chatbots can be differentiated 
by their knowledge-base, service etc. According to the 
knowledge base, this chatbot is **closed-domain** as this
chatbot can only give responses for a specific domain. And 
according to the service, it is an **intrapersonal** 
chatbot as this is made for giving service to students.

There are 3 types of models that are used to produce 
the appropriate response 
 - **Rule-based model** 
 - **Retrieval-based model**, and 
 - **Generative model**. 

In this case, I used **Retrieval-based** model as this chatbot give
responses by querying a database.






## Deployment

This chatbot is deployed as a telegram bot. you can run 
this chatbot by running the **telebot.py** python script.
After that, you have to search in telegram by typing 
**departmental_bot** and you are ready to go.


## Authors

- [Subhradeep Rang](https://github.com/srang992)

