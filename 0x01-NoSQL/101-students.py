#!/usr/bin/env python3
""" mongodb with Python by pymongo """


def top_students(mongo_collection):
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students
