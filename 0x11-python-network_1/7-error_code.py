#!/usr/bin/python3

"""
Python script that takes in a URL, sends a GET request
to the URL, and displays the body of the response.

Usage:
    python script.py <url>

Arguments:
    <url>: The URL to send the GET request to.
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
