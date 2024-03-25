#!/usr/bin/env python3
""" mongodb with Python by pymongo """

from pymongo import MongoClient

def log_stats(mongo_collection):
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Counting methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Counting status checks
    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print("{} status check".format(status_check_count))

    # Top 10 IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(mongo_collection.aggregate(pipeline))
    for ip_data in top_ips:
        ip = ip_data['_id']
        count = ip_data['count']
        print("\t{}: {}".format(ip, count))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)
