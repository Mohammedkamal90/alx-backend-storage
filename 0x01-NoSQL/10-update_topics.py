#!/usr/bin/env python3
""" mongodb with Python by pymongo """


def update_topics(mongo_collection, name, topics):
    # Update topics of a school document based on the name
    result = mongo_collection.update_many(
        {"name": name},  # Filter criteria
        {"$set": {"topics": topics}}  # Update document
    )
    return result.modified_count
