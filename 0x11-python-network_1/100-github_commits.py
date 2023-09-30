#!/usr/bin/python3
import requests
import sys

# Extract the repository name and owner name from command-line arguments
repository_name = sys.argv[1]
owner_name = sys.argv[2]

# Define the GitHub API URL for listing commits
url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

# Set the parameters to get the most recent 10 commits
params = {"per_page": 10, "page": 1}

try:
    # Send a GET request to the GitHub API
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        commits = response.json()

        # Print the list of commits with their SHA and author names
        for commit in commits:
            sha = commit.get("sha")
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    # Handle the case where the request fails
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
