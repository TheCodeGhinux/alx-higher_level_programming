#!/usr/bin/python3
import requests
import sys

# Extract the username and personal access token (PAT) from command-line arguments
username = sys.argv[1]
pat = sys.argv[2]

# Construct the URL for the GitHub API to get user information
url = f"https://api.github.com/user"

# Set up Basic Authentication with the PAT as the password
auth = (username, pat)

try:
    # Send a GET request to the GitHub API
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        user_data = response.json()

        # Display the user ID
        user_id = user_data.get("id")
        print(f"Your GitHub user ID is: {user_id}")

    # Handle the case where the request fails
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
