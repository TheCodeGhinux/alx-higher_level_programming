#!/usr/bin/python3
"""
Python script that takes in a letter
and sends a POST request
to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # Extract the letter from command-line
    # arguments or set it to an empty string if not provided
    input_word = "" if len(sys.argv) == 1 else sys.argv[1]
    search = {"q": input_word}

    res= requests.post("http://0.0.0.0:5000/search_user", data=search)
    try:
        if res.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.json().get("id"), res.json().get("name")))
    except ValueError:
        print("Not a valid JSON")