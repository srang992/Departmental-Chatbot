"""
required file for chatbot to work properly
"""
import sqlite3
import random
from main_files.responses import *


def find_courses(params):
    """
    function responsible for finding course from database
    :param params: dictionary
    :return: results from database
    """
    query = "SELECT * FROM courses"
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " WHERE " + " AND ".join(filters)

    t = tuple(params.values())
    conn = sqlite3.connect("database/makaut_data.sqlite")
    c = conn.cursor()
    c.execute(query, t)
    return c.fetchall()


def slot_course_response(message, param_dict, interpreter, response_list):
    """
    responsible for giving the power of slot response
    :param response_list: list of responses
    :param message: user message
    :param param_dict: dictionary consisting query parameters
    :param interpreter: main_files model
    :return: response
    """
    entities = interpreter.parse(message)['entities']
    for ent in entities:
        param_dict[ent['entity']] = str(ent['value'])
    results = find_courses(param_dict)
    names = [r[0] for r in results]
    n = min(len(results), 3)
    return response_list[n].format(*names), param_dict, names, n


def concat_upper(params):
    """
    function responsible for making query parameters
    :param params: dictionary of queries
    :return: final list
    """
    filter1 = []
    filter2 = []
    for key, value in params.items():
        if type(value) == str and not value.isupper():
            filter1 += ["{}=?".format(key)]
        else:
            filter1 += ["{} IS NOT ?".format(key)]

    main_filter = filter1 + filter2
    return main_filter


def find_pg_fees(params):
    """
    this function helps chatbot to find pg course fees from the database
    :param params: dictionary of query parameters
    :return: responses
    """
    query = ""
    if len(params) > 0:
        columns = ["{}".format(c) for c in params.keys()]
        filters = concat_upper(params)
        query += "SELECT course_name," + ",".join(columns) + " FROM pg_fee_table " + " WHERE " \
                 + " AND ".join(filters)

    t = tuple(params.values())
    conn = sqlite3.connect("database/makaut_data.sqlite")
    c = conn.cursor()
    c.execute(query, t)
    return c.fetchall()


def find_ug_fees(params):
    """
    this function helps chatbot to find ug course fees from the database
    :param params: dictionary of query parameters
    :return: responses
    """
    query = ""
    if len(params) > 0:
        columns = ["{}".format(c) for c in params.keys()]
        filters = concat_upper(params)
        query += "SELECT course_name," + ",".join(columns) + " FROM bsc_fee_table " + " WHERE " \
                 + " AND ".join(filters)

    t = tuple(params.values())
    conn = sqlite3.connect("database/makaut_data.sqlite")
    c = conn.cursor()
    c.execute(query, t)
    return c.fetchall()


def slot_less_pg_respond(user_message, interpreter, response_list):
    """
    slot less response for pg courses
    :param user_message: message given by user
    :param interpreter: trained model
    :param response_list: list of response
    :return: response
    """
    entities = interpreter.parse(user_message)['entities']
    params = {}
    for ent in entities:
        params[ent['entity']] = str(ent['value'])

    results = find_pg_fees(params)
    names = [r[0] for r in results]
    tuition_amount = [r[1] for r in results]
    n = min(len(results), 1)
    if len(names) != 0 and len(tuition_amount) != 0:
        return response_list[n].format(names[0], tuition_amount[0]), names, tuition_amount, n
    else:
        return "I'm sorry :( I couldn't find anything like that"


def slot_less_ug_respond(user_message, interpreter, response_list):
    """
    slot less response for ug courses
    :param user_message: message given by user
    :param interpreter: trained model
    :param response_list: list of responses
    :return: response
    """
    entities = interpreter.parse(user_message)['entities']
    params = {}
    for ent in entities:
        params[ent['entity']] = str(ent['value'])

    results = find_ug_fees(params)
    names = [r[0] for r in results]
    tuition_amount = [r[1] for r in results]
    n = min(len(results), 1)
    print(params)
    if len(names) != 0 and len(tuition_amount) != 0:
        return response_list[n].format(names[0], tuition_amount[0]), names, tuition_amount, n
    else:
        return "I'm sorry :( I couldn't find anything like that"


def get_response(msg, interpreter, param_value):
    """
    function for responding the user message.
    :param interpreter: trained model
    :param param_value: dictionary
    :param msg: user messages.
    :return:
    """
    intent = interpreter.parse(msg)['intent']['name']
    if intent == 'greetings':
        return random.choice(hello_responses)
    if intent == 'makaut_course_search':
        response, param_value, names, count = slot_course_response(msg, param_value, interpreter, data_responses)
        # print(param_value)
        return response
    if intent == "ask_for_pg_course_total_fee":
        response, names, tuition_amount, count = slot_less_pg_respond(msg, interpreter, total_fees_responses)
        return response
    if intent == "ask_for_pg_course_tuition_fee":
        response, names, tuition_amount, count = slot_less_pg_respond(msg, interpreter, tuition_fees_responses)
        return response
    if intent == "ask_for_pg_course_admission_fee":
        response, names, tuition_amount, count = slot_less_pg_respond(msg, interpreter, admission_fees_responses)
        return response
    if intent == "ask_for_bsc_course_tuition_fee":
        response, names, tuition_amount, count = slot_less_ug_respond(msg, interpreter, tuition_fees_responses)
        return response
    if intent == "ask_for_bsc_course_admission_fee":
        response, names, tuition_amount, count = slot_less_ug_respond(msg, interpreter, admission_fees_responses)
        return response
    if intent == "ask_for_bsc_course_total_fee":
        response, names, tuition_amount, count = slot_less_ug_respond(msg, interpreter, total_fees_responses)
        return response
    if intent == 'thank you':
        return random.choice(thank_you_responses)
    if intent == 'whereabouts':
        return random.choice(whereabouts_responses)
    if intent == 'ask_my_health':
        return random.choice(ask_responses)
    if intent == 'goodbyes':
        return random.choice(goodbye_responses)
    if intent == "exam_related_query":
        return "Right now I have no information about this. You have to wait 4 to 5 months for that.", intent
