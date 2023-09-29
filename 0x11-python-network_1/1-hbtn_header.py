#!/usr/bin/python3
"""
    Python script that takes in a URL
    sends a request to the URL and displays the value
"""

import urllib.request
import sys

""" Checking if URL is inputed as argument """
if len(sys.argv) != 2:
    print("Usage: python 1-hbtn_header.py <URL>")
    sys.exit(1)

input_url = sys.argv[1]

try:
    with urllib.request.urlopen(input_url) as response:
        """ Get the value of the header"""
        req_id = response.getheader('X-Request-Id')
        if req_id is not None:
            print(req_id)
except Exception as e:
    print(f"Error: {e}")
