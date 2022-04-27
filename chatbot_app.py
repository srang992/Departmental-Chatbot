
import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["chatbot_data"]

collection = db["data"]

entities = []

text = input("\n Enter text: ")

intent = input("\n Enter intent: ")

entity_count = int(input("\n Enter entity count: "))

print("\n")

if entity_count == 0:
    entities = []
else:
    for i in range(0, entity_count):

        print("________________ ENTITY NO {} ________________\n".format(i+1))
        entity_name = input("Enter entity name: ")
        entity_value_text = input("Enter entity value available in text: ")
        entity_value = input("Enter entity value: ")
        start = text.index(entity_value_text.lower())
        end = text.index(entity_value_text.lower()) + len(entity_value_text.lower())

        entity = {"end": end, "entity": entity_name, "start": start, "value": entity_value}

        entities.append(entity)

        print("\n")

data = {"text": text, "intent": intent, "entities": entities}

pprint(data)
print("\n")

confirm = input("Do you want to insert this in MongoDB?: ")

if confirm == "Y" or confirm == "Yes" or confirm == "y" or confirm == "yes":
    collection.insert_one(data)
    print("Inserted!")
else:
    print("Data is not inserted in MongoDB")

