#!/usr/bin/env python3

"""MongoDB with Python by pymongo"""
from pymongo import MongoClient

def print_nginx_logs_stats(nginx_collection):
    """Prints stats about Nginx logs"""
    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status checks
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")

def main():
    """Main function"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    print_nginx_logs_stats(nginx_collection)

if __name__ == "__main__":
    main()
