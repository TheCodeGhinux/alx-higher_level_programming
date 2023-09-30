#!/usr/bin/python3

"""Python script that send a web req"""

import requests
import sys

input_url = sys.argv[1]

try:
    res = requests.get(input_url)
    print(res.text)

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")

except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
