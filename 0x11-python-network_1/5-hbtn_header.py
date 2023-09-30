#!/usr/bin/python3

"""
    Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the variable X-Request-Id
    in the response header
"""

import requests
import sys

# Check if a url is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

input_url = sys.argv[1]

try:
    res = requests.get(input_url)

    # Get value of the X-Request-Id header
    x_request_id = res.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
