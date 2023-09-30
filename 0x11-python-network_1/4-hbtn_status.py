#!/usr/bin/python3
"""
    Python script that fetches from url
"""

import requests

# Input url
input_url = 'https://alx-intranet.hbtn.io/status'

try:
    res = requests.get(input_url)
    res.raise_for_status()

    # Display the response body with tabulation
    print(f"""
    Body response:\n\t- type: {type(res.text)}\n\t- content: {res.text}
    """)
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
