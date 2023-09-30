#!/usr/bin/python3
"""Python script that sends a web req with error handling"""

import requests
import sys

try:
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)

