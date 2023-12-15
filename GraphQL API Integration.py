import requests
import json

# Define the corrected GraphQL endpoint for SWAPI
graphql_endpoint = 'https://swapi-graphql.netlify.app/.netlify/functions/index'

# Define the corrected GraphQL query to get information about a character
query = '''
{
  person(personID: 1) {
    name
    birthYear
    eyeColor
  }
}
'''

# Create the GraphQL request
data = {'query': query}
response = requests.post(graphql_endpoint, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=2))
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
