from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from main_files.chat import *

app = Flask(__name__)


@app.get('/')
def home():
    return "Welcome to the Chatbot!"


@app.post('/predict')
def predict():

    user_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    answer = get_response(user_msg, interpreter=interpreter, param_value=param_val)
    response.message(answer)
    return str(response)


if __name__ == '__main__':
    app.run()
