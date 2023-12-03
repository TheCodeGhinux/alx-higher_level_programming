#!/usr/bin/python3
"""
    Python script that takes 2 arguments in order to
    solve an interview challenge
"""
import requests
import sys


if __name__ == "__main__":
    """
      Extract the repo name and owner
      name from command-line arguments
    """
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    input_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    res = requests.get(input_url)
    commits = res.json()
    try:
        for req in range(10):
            print("{}: {}".format(
                commits[req].get("sha"),
                commits[req].get("commit").get("author").get("name")))
    except IndexError:
        pass
