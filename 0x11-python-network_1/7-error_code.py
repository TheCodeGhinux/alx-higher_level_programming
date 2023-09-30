#!/usr/bin/python3

"""
     Python script that takes in a url, sends a request
     to the url and displays the body of the response.
"""

import requests
import sys

# Get url from command-line arguments
input_url = sys.argv[1]

try:
    # Send a GET request to the url
    res = requests.get(input_url)

    # Display the res body
    print(res.text)

    # Check the HTTP status code
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")

except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
