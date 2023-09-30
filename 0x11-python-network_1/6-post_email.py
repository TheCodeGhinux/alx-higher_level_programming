#!/usr/bin/python3

"""
    Python script that takes in a url, sends a
    request to the url and displays the value
    of the variable X-Request-Id in the response header
"""

import requests
import sys

# Check for the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python 6-post_email.py <input_url> <input_email>")
    sys.exit(1)

# Get url and email from command-line arguments
input_url = sys.argv[1]
input_email = sys.argv[2]

# Create a dictionary with the email parameter
data = {"email": input_email}

try:
    # Send a POST request with the email
    res = requests.post(input_url, data=data)

    # Check if the request was successful (status code 200)
    if res.status_code == 200:
        # Show the response body
        print(res.text)
    else:
        print(f"Error: Received status code {res.status_code}")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
