#!/usr/bin/python3
import requests
import sys

""" Extract the letter from command-line arguments,
or set it to an empty string if not provided"""
if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

# Create a dictionary with the letter parameter
data = {"q": letter}

# input url to send the POST request
input_url = "http://0.0.0.0:5000/search_user"

try:
    # Send a POST request with the letter parameter
    res = requests.post(input_url, data=data)

    # Check if the response contains valid JSON and is not empty
    if res.headers.get("content-type") == "application/json" and res.text:
        res_json = res.json()

        # Check for the JSON 'id' and 'name' keys
        if "id" in res_json and "name" in res_json:
            user_id = res_json["id"]
            user_name = res_json["name"]
            print(f"[{user_id}] {user_name}")
        else:
            print("Not a valid JSON")

    # Handle empty case
    elif not res.text:
        print("No result")

    # Handle error if response is not available
    else:
        print("Not a valid JSON")

except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
