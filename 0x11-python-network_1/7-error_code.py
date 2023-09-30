#!/usr/bin/python3
"""send a web req with error handling"""

import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code > 400:
        print(f"Error code: {res.status_code}")
    else:
        print(response.text)
