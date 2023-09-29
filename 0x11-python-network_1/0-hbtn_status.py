#!/usr/bin/python3

"""
    Python Script to fetch from a url
"""

import urllib.request

input_url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(input_url) as response:
        html_res = response.read()
        print(f"""Body response:\n\t- type: {type(html_res)}
        \n\t- content: {html_res.decode('utf-8')}""")
except Exception as e:
    print(f"Error: {e}")
