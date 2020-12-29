import pymongo
from keys import *
import json
from pymongo import MongoClient
from pprint import pprint

db = cluster["KuriusHacks"]
collection = db["Events"]

"""
What it does:
    - This function adds a new event to the database
      It will add the name of the event, who, when, etc.

Parameters:
    - Name of event (ex: "CSUSM Food Drive")
    - Where is the event (ex: "123 Cougar Lane")
    - When is the event

Return:
    - Does not return anything
"""


def add_Event_To_Database(nameOfEvent, addressOfEvent, dateOfEvent, descOfEvent, contactInfo):
    FoodDriveEvent = {
        'nameOfEvent': nameOfEvent,
        'addressOfEvent': addressOfEvent,
        'dateOfEvent': dateOfEvent,
        'descOfEvent': descOfEvent,
        'contactInfo': contactInfo
    }
    collection.insert_one(FoodDriveEvent)
    print("Added event to database")



def preview_database():
    events = []
    results = collection.find({})
    #results = data.json()
    for x in results:
        events.append(x)
    return events
