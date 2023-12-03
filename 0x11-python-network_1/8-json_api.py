#!/usr/bin/python3
"""
Python script that takes in a letter
and sends a POST request
to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    # Define the URL for the POST request
    url = "http://0.0.0.0:5000/search_user"

    # Extract the letter from command-line
    # arguments or set it to an empty string if not provided
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    # Create a dictionary with the 'q' parameter
    search = {'q': q}

    # Send the POST request
    req = requests.post(url, data=search)

    try:
        # Parse the JSON response
        res = req.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if isinstance(res, list) and len(res) < 1:
            print('No result')
        else:
            # Access the 'id' and 'name' from the JSON response
            print('[{}] {}'.format(res[0]['id'], res[0]['name']))
