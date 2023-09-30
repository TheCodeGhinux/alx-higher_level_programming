#!/usr/bin/python3
import requests
import sys

# Extract URL from command-line arguments
url = sys.argv[1]

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Display the response body
    print(response.text)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
