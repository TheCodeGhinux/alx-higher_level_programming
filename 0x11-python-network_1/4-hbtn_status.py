#!/usr/bin/python3
"""
    Python script that fetches from url
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

try:
    response = requests.get(url)
    response.raise_for_status()

    # Display the response body with tabulation
    print(f"Body response:\n\t- type: {type(response.text)}\n\t- content: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
