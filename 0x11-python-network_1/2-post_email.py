#!/usr/bin/python3
"""
    Python script that takes in a URL and an email
    sends a POST request to the passed URL with
    the email as a parameter, and
    displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys

"""
    Check if both a URL and an
    email are provided as arguments
"""

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send a POST request with the email parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        html = response.read().decode('utf-8')
        print(html)
except Exception as e:
    print(f"Error: {e}")
