#!/usr/bin/python3

"""
     Python script that takes your GitHub credentials
     (username and password) and uses the GitHub API to display your id
"""

import requests
import sys

""" Extract the username and personal access token
from command-line arguments"""
usr_name = sys.argv[1]
token = sys.argv[2]

# input url for the GitHub API to get user info
input_url = f"https://api.github.com/user"

# Set up Basic Authentication with the token as the password
auth = (usr_name, token)

try:
    # Send a GET request to the GitHub API
    res = requests.get(input_url, auth=auth)

    # Check if the request was successful (status code 200)
    if res.status_code == 200:
        user_data = res.json()

        # Display the user ID
        user_id = user_data.get("id")
        print(f"Your GitHub user ID is: {user_id}")

    # Handle error on failure
    else:
        print(f"Error: Received status code {res.status_code}")

except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
