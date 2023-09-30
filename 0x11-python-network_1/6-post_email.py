#!/usr/bin/pythn3
import requests
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

# Extract URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {"email": email}

try:
    # Send a POST request with the email parameter
    response = requests.post(url, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Display the response body
        print(response.text)
    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
