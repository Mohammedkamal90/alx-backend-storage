#!/usr/bin/env python3
""" mongodb with Python by pymongo """

def insert_school(mongo_collection, **kwargs):
    # Insert a new document into the collection
    result = mongo_collection.insert_one(kwargs)
    
    # Return the new _id
    return result.inserted_id
