#!/usr/bin/python3
import requests
import sys

# Check if a URL is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
