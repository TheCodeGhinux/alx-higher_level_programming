#!/usr/bin/python3
"""
    Python script that takes in a URL
"""

import requests
import sys

if __name__ == '__main__':
    # Get URL from command-line arguments
    input_url = sys.argv[1]
    res = requests.get(input_url)
    if res.status_code > 400:
         print(f"Error code: {res.status_code}")
    else:
        print(res.text)
