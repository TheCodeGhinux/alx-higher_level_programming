#!/usr/bin/python3

"""
    Python script that takes 2 arguments in order to
    solve an interview challenge
"""

import requests
import sys

"""
    Extract the repo name and owner 
    name from command-line arguments
"""
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Define the GitHub API URL for listing commits
input_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

# Set the parameters to get the most recent 10 commits
params = {"per_page": 10, "page": 1}

try:
    # Send a GET request to GitHub
    res = requests.get(input_url, params=params)

    """ Check if request was successful
    and return status code 200 """
    if res.status_code == 200:
        commits = res.json()

        # Print list of commits with their SHA and author names
        for commit in commits:
            sha = commit.get("sha")
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    # Handle error for failure
    else:
        print(f"Error: Received status code {res.status_code}")

except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
