#!/usr/bin/python3
"""
    Python script that takes in a URL
    sends a request to the URL and displays the value
"""

import urllib.request
import sys

""" Check if a URL is provided as an argument """
if len(sys.argv) != 2:
    print("Usage: python 1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        """ Get the value of the X-Request-Id header"""
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id is not None:
            print(x_request_id)
except Exception as e:
    print(f"Error: {e}")
