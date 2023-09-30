#!/usr/bin/python3
"""Python script that sends a web req with error handling"""

import requests
import sys

"""Python script that sends a web req with error handling"""
try:
    """Python script that sends a web req with error handling"""
    res = requests.get(sys.argv[1])
    """Python script that sends a web req with error handling"""
    if res.status_code > 400:
        """Python script that sends a web req with error handling"""
        print(f"Error code: {res.status_code}")
    """Python script that sends a web req with error handling"""
    else:
        """Python script that sends a web req with error handling"""
        print(res.text)

"""Python script that sends a web req with error handling"""
except requests.exceptions.RequestException as err:
    """Python script that sends a web req with error handling"""
    print(f"Error: {err}")
