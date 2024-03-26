#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

def count_logs_by_method(collection):
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    return {doc["_id"]: doc["count"] for doc in collection.aggregate(pipeline)}

def count_status_check(collection):
    return collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    print('Methods:')
    method_counts = count_logs_by_method(nginx_collection)
    for method, count in method_counts.items():
        print(f'\tmethod {method}: {count}')

    status_check = count_status_check(nginx_collection)
    print(f'{status_check} status check')
