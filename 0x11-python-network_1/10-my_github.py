#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """ Extract the username and personal access token
    from command-line arguments"""
    usr_name = sys.argv[1]
    token = sys.argv[2]
    auth = HTTPBasicAuth(usr_name, token)
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
