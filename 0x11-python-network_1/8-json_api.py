#!/usr/bin/python3

"""
    Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

# input url to send the POST request
url = "http://0.0.0.0:5000/search_user"

""" Extract the letter from command-line arguments,
or set it to an empty string if not provided"""
if len(sys.argv) < 2:
    search = {'q': '""'}
else:
    search = {'q': sys.argv[1]}

req = requests.post(url, search)

try:
    search = req.json()
except ValueError:
    print("Not a valid JSON")
else:
    if isinstance(search, list) and len(search) < 1:
        print('No result')
    else:
        print(f"[{user['id']}] {user['name']}")




