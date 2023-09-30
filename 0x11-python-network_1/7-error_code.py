#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response.
"""

import requests
import sys

# Get URL from command-line arguments
input_url = sys.argv[1]

if __name__ == '__main__':
    res = requests.get(input_url)
    if res.status_code > 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
