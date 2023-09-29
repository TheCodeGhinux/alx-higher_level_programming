#!/usr/bin/python3

"""
     Python script that takes in a URL
     sends a request to the URL and
     displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.error
import sys

"""
    To check if url is inputted
"""

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

input_url = sys.argv[1]

try:
    with urllib.request.urlopen(input_url) as res:
        """ Read the body
        """
        html_res = res.read().decode('utf-8')
        print(html_res)
except urllib.error.HTTPError as err:
    print(f"Error code: {err.code}")
except Exception as err:
    print(f"Error: {err}")
