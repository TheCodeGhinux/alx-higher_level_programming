#!/usr/bin/python3

"""
    Python Script to fetch from a url
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(f"""Body response:\n\t- type: {type(html)}
        \n\t- content: {html.decode('utf-8')}""")
except Exception as e:
    print(f"Error: {e}")
