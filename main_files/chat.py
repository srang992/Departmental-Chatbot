"""
This file contains required function for chatting
"""
from rasa_nlu.model import Interpreter
from main_files.functions import *

interpreter = Interpreter.load("model/default/chatbot_model")
param_val = {}

if __name__ == '__main__':
    while True:
        text = input('You: ')
        responses = get_response(text, interpreter, param_value=param_val)
        print("Mike: {}".format(responses))
