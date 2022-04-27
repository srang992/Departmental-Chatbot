"""
This file contains required function for chatting
"""
from rasa_nlu.model import Interpreter
from main_files.functions import *

interpreter = Interpreter.load("test_models/apr_27_1/default/chatbot_model")
param_val1 = {}

if __name__ == '__main__':
    while True:
        text = input('You: ')
        responses = get_response(text, interpreter, param_value=param_val)
        print("Mike: {}".format(responses))
