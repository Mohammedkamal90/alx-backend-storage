#!/usr/bin/env python3
""" mongodb with Python by pymongo """


# 11-schools_by_topic.py

def schools_by_topic(mongo_collection, topic):
    # Find all documents in the collection that contain the specified topic
    schools = mongo_collection.find({"topics": topic})

    # Convert cursor to list of documents
    schools_list = [school for school in schools]

    return schools_list
