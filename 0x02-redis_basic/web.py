#!/usr/bin/env python3
"""
web cache
"""

import requests
import redis
import time

# Connect to Redis
redis_client = redis.Redis()

def get_page(url: str) -> str:
    # Track the number of times the URL is accessed
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    # Check if the page is cached
    cached_page = redis_client.get(url)
    if cached_page:
        return cached_page.decode('utf-8')

    # Fetch the page content
    response = requests.get(url)
    page_content = response.text

    # Cache the page content with a 10-second expiration
    redis_client.setex(url, 10, page_content)

    return page_content

if __name__ == "__main__":
    # Test the get_page function
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    start_time = time.time()
    page_content = get_page(url)
    end_time = time.time()

    print(f"Page content:\n{page_content}")
    print(f"Time taken: {end_time - start_time} seconds")

    # Wait for 5 seconds and fetch the page again
    time.sleep(5)
    start_time = time.time()
    page_content = get_page(url)
    end_time = time.time()

    print(f"Page content:\n{page_content}")
    print(f"Time taken: {end_time - start_time} seconds")
