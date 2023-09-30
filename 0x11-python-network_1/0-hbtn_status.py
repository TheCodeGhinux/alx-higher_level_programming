#!/usr/bin/python3

"""
    Python Script to fetch from a url
"""

import urllib.request

input_url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(input_url) as response:
        html_res = response.read()
        html_type = type(html)
        print("Body response:")
        print("\t- type: {}".format(html_type))
        print("\t- content: {}".format(html_res))
        print("\t- utf8 content: {}".format(html_res.decode('utf-8')))
except Exception as e:
    print(f"Error: {e}")
