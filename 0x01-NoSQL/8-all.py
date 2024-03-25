#!/usr/bin/env python3
"""mongodb with python by pymongo"""


def list_all(mongo_collection):
    # Find all documents in the collection
    documents = mongo_collection.find({})


    documents_list = [doc for doc in documents]
    
    return documents_list
