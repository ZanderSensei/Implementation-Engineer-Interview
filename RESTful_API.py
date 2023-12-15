import requests

# API base URL
base_url = "https://jsonplaceholder.typicode.com"

# Endpoint to get a list of users
endpoint = "/users"

# Full URL for the request
url = base_url + endpoint

try:
    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the JSON response
        print("API Response:")
        print(response.json())
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    # Handle exceptions (e.g., connection errors)
    print(f"Error: {e}")
