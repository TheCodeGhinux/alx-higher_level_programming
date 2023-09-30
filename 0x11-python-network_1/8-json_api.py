#!/usr/bin/python3
import requests
import sys

# Extract the letter from command-line arguments, or set it to an empty string if not provided
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

# Create a dictionary with the letter parameter
data = {"q": q}

# Define the URL to send the POST request to
url = "http://0.0.0.0:5000/search_user"

try:
    # Send a POST request with the letter parameter
    response = requests.post(url, data=data)

    # Check if the response contains valid JSON and is not empty
    if response.headers.get("content-type") == "application/json" and response.text:
        # Parse the JSON response
        response_json = response.json()

        # Check if the JSON contains 'id' and 'name' keys
        if "id" in response_json and "name" in response_json:
            user_id = response_json["id"]
            user_name = response_json["name"]
            print(f"[{user_id}] {user_name}")
        else:
            print("Not a valid JSON")

    # Handle the case where the JSON is empty
    elif not response.text:
        print("No result")

    # Handle the case where the response is not valid JSON
    else:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
