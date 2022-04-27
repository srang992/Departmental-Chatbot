
import json
import pymongo

if __name__ == '__main__':
    print("Welcome to PyMongo!\n")

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["chatbot_data"]

    collection = db["data"]

    chat_data = {"rasa_nlu_data": {"common_examples": []}}

    results = collection.find({}, {"_id": 0})

    for item in results:
        chat_data["rasa_nlu_data"]["common_examples"].append(item)

    print(chat_data)

    with open("chattydata.json", "w") as f:
        json.dump(chat_data, f)

    # collection.delete_many({"intent": "ask_for_bsc_course_total_fee"})
    #
    # print("deleted!")

