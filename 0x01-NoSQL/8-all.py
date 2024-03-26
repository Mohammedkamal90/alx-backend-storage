#!/usr/bin/env python3
"""mongodb with python by pymongo"""


def list_all(mongo_collection):
    """ Find all documents in the collection
    """
    return [doc for doc in mongo_collection.find()]
