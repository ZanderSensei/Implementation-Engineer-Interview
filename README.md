# Implementation-Engineer-Interview
Contains section A of the interview

Question 1
Give examples of different integration protocols you have come across and give 
example scripts in python 3 on how to achieve each one.

Introduction

Integrating systems Involve using different Protocols based on Technology. 

Example 1: RESTful API Integration
This is an interface that two computer systems use to exchange information securely over the internet
This protocol is used in HTTP/HTTPS

Code in Python
----------------

#Start by importing request i.e GET
import requests 

# API base URL link
base_url = "https://jsonplaceholder.typicode.com"

# Endpoint to get a list of users
endpoint = "/users"

# Full URL for the request
url = base_url + endpoint

try:
    # Make a GET request to the API11:45 AM 12/13/2023
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



Result
------
API Response:
[{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}, {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}, {'id': 3, 'name': 'Clementine Bauch', 'username': 'Samantha', 'email': 'Nathan@yesenia.net', 'address': {'street': 'Douglas Extension', 'suite': 'Suite 847', 'city': 'McKenziehaven', 'zipcode': '59590-4157', 'geo': {'lat': '-68.6102', 'lng': '-47.0653'}}, 'phone': '1-463-123-4447', 'website': 'ramiro.info', 'company': {'name': 'Romaguera-Jacobson', 'catchPhrase': 'Face to face bifurcated interface', 'bs': 'e-enable strategic applications'}}, {'id': 4, 'name': 'Patricia Lebsack', 'username': 'Karianne', 'email': 'Julianne.OConner@kory.org', 'address': {'street': 'Hoeger Mall', 'suite': 'Apt. 692', 'city': 'South Elvis', 'zipcode': '53919-4257', 'geo': {'lat': '29.4572', 'lng': '-164.2990'}}, 'phone': '493-170-9623 x156', 'website': 'kale.biz', 'company': {'name': 'Robel-Corkery', 'catchPhrase': 'Multi-tiered zero tolerance productivity', 'bs': 'transition cutting-edge web services'}}, {'id': 5, 'name': 'Chelsey Dietrich', 'username': 'Kamren', 'email': 'Lucio_Hettinger@annie.ca', 'address': {'street': 'Skiles Walks', 'suite': 'Suite 351', 'city': 'Roscoeview', 'zipcode': '33263', 'geo': {'lat': '-31.8129', 'lng': '62.5342'}}, 'phone': '(254)954-1289', 'website': 'demarco.info', 'company': {'name': 'Keebler LLC', 'catchPhrase': 'User-centric fault-tolerant solution', 'bs': 'revolutionize end-to-end systems'}}, {'id': 6, 'name': 'Mrs. Dennis Schulist', 'username': 'Leopoldo_Corkery', 'email': 'Karley_Dach@jasper.info', 'address': {'street': 'Norberto Crossing', 'suite': 'Apt. 950', 'city': 'South Christy', 'zipcode': '23505-1337', 'geo': {'lat': '-71.4197', 'lng': '71.7478'}}, 'phone': '1-477-935-8478 x6430', 'website': 'ola.org', 'company': {'name': 'Considine-Lockman', 'catchPhrase': 'Synchronised bottom-line interface', 'bs': 'e-enable innovative applications'}}, {'id': 7, 'name': 'Kurtis Weissnat', 'username': 'Elwyn.Skiles', 'email': 'Telly.Hoeger@billy.biz', 'address': {'street': 'Rex Trail', 'suite': 'Suite 280', 'city': 'Howemouth', 'zipcode': '58804-1099', 'geo': {'lat': '24.8918', 'lng': '21.8984'}}, 'phonebsite': 'conrad.com', 'company': {'name': 'Yost and Sons', 'catchPhrase': 'Switchable contextually-based project', 'bs': 'aggregate real-time technologies'}}, {'id': 10, 'name': 'Clementina DuBuque', 'username': 'Moriah.Stanton', 'email': 'Rey.Padberg@karina.biz', 'address': {'street': 'Kattie Turnpike', 'suite': 'Suite 198', 'city': 'Lebsackbury', 'zipcode': '31428-2261', 'geo': {'lat': '-38.2386', 'lng': '57.2232'}}, 'phone': '024-648-3804', 'website': 'ambrose.net', 'company': {'name': 'Hoeger LLC', 'catchPhrase': 'Centralized empowering task-force', 'bs': 'target end-to-end models'}}]

The API has printed a List of all the users including their details

Example 2: SOAP web Service Calculator
SOAP protocol is XML based protocol used for accessing web services over HTTP

code in python
--------------

#Zeep is used to pass reqest and convert it to final xml format
from zeep import Client

# Define the SOAP service URL
service_url = "http://www.dneonline.com/calculator.asmx?WSDL"

# Create a SOAP client
client = Client(service_url)

# Specify the numbers for addition
num1 = 5
num2 = 10

try:
    # Call the SOAP operation (Add)
    result = client.service.Add(num1, num2)

    # Print the result
    print(f"Result of {num1} + {num2} is: {result}")

except Exception as e:
    # Handle exceptions
    print(f"Error: {e}")

Result
------
Result of 5 + 10 is: 15


Example 3: GraphQL API Integration
GraphQL is a questy language for API's  to fulfil queries with existing data

code in python
--------------
import requests
#python needs to import json to work with JSON data
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

Result
------
{
  "data": {
    "person": {
      "name": "Luke Skywalker",
      "birthYear": "19BBY",
      "eyeColor": "blue"
    }
  }
}


Question 3
Give examples of different encryption/hashing methods you have come across and example scripts in python 3 on how to achieve each one

1.MD5 Hashing
This is a commonly used one-way hashing algorithm 

Python code
-----------

#import library for efficient hashing of a file
import hashlib

#create hashing function
def md5_hash(input_text):
    md5_hasher = hashlib.md5()
    md5_hasher.update(input_text.encode('utf-8'))
    return md5_hasher.hexdigest()

# Example usage with text
input_text = "Hello, World!"
hashed_result = md5_hash(input_text)

#Print the result
print(f'MD5 Hash: {hashed_result}')

Result
------
MD5 Hash: 65a8e27d8879283831b664bd8b7f0ad4

2.AES Hashing
AES is a symmetric encryption algorithm used for securing sensitive data


python code
-----------
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

#create function for encryption and the key
def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return b64encode(nonce + tag + ciphertext).decode('utf-8')

#create function for decryption and the key
def aes_decrypt(encrypted_text, key):
    data = b64decode(encrypted_text.encode('utf-8'))
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_text = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_text.decode('utf-8')

# Example usage with text
input_text = "Sensitive Information"
encryption_key = get_random_bytes(16)  # 128-bit key for AES-128
encrypted_result = aes_encrypt(input_text, encryption_key)
decrypted_result = aes_decrypt(encrypted_result, encryption_key)

#Print input data, encrypted result and decrypted result
print(f'Original Text: {input_text}')
print(f'Encrypted Text: {encrypted_result}')
print(f'Decrypted Text: {decrypted_result}')


Result
------
Original Text: Sensitive Information
Encrypted Text: 9nfZHiM3/1ITVSxuGckYliDtrX9yShJIHqgm/GdslulVhIL8W4ggQ9kfGbElwYoqk99Gpw=
Decrypted Text: Sensitive Information


Question 2

Give a walkthrough of how you will manage a data streaming application sending 
one million notifications every hour while giving examples of technologies and 
configurations you will use to manage load and asynchronous services.

1. Requirements Analysis:
Understand the nature of notifications (size, content, delivery urgency).
Define the target platforms (mobile, web, email).
Determine the frequency and volume of notifications.


2. Technological Stack:
Messaging Queue:

-Utilize a message queue for asynchronous processing.
Example: RabbitMQ, Apache Kafka.
Database:

-Choose a database for storing notification data and user preferences.
Example: MongoDB, Cassandra.
Real-Time Processing:

-Use a real-time processing framework for immediate actions.
Example: Apache Flink, Apache Storm.
Notification Service:

-Implement a service to send notifications based on user preferences.
Example: Firebase Cloud Messaging (FCM), Amazon SNS.
Load Balancing:

-Employ load balancing for distributing incoming requests.
Example: Nginx, HAProxy.
Monitoring:

-Integrate monitoring tools for tracking system health.
Example: Prometheus, Grafana.


3. Architecture Design:

-Microservices:
Design microservices for modular and scalable components.
Separate services for notification generation, processing, and delivery.

-Asynchronous Processing:
Implement asynchronous processing to decouple components.
Use message queues to manage the flow of notifications.

-Scalability:
Design for horizontal scalability to handle increasing loads.
Use containerization (Docker) and orchestration (Kubernetes).

4. Configuration Examples:
Nginx Load Balancing (Example):
# nginx.conf
http {
  upstream notification_servers {
    server backend1.example.com;
    server backend2.example.com;
    # Add more servers as needed
  }

  server {
    listen 80;

    location / {
      proxy_pass http://notification_servers;
    }
  }
}

5. Scaling and Load Management:
Horizontal Scaling:

Deploy multiple instances of services to distribute the load.
Use container orchestration for automatic scaling.
Caching:

Implement caching mechanisms to reduce redundant processing.
Use Redis for caching frequently accessed data.


6. Monitoring and Optimization:
Log Aggregation:

Aggregate logs for centralized monitoring and debugging.
Use ELK Stack (Elasticsearch, Logstash, Kibana).
Performance Optimization:

Regularly analyze system performance and optimize as needed.
Identify bottlenecks and address them proactively.

7. Security Considerations:
Authentication and Authorization:

Implement secure authentication and authorization mechanisms.
Use OAuth or JWT for token-based authentication.
Data Encryption:

Encrypt sensitive data during transit and storage.
Implement TLS for communication.

8. Testing:
Unit Testing:

Implement thorough unit testing for each component.
Use testing frameworks like JUnit or Pytest.
Load Testing:

Conduct load testing to simulate real-world conditions.
Use tools like Apache JMeter or Gatling.

9. Documentation:
README Updates:
Keep the README.md file up-to-date with installation and configuration instructions.
Include examples, commands, and troubleshooting steps.

10. Continuous Integration/Continuous Deployment (CI/CD):
Automate Deployment:
Utilize CI/CD pipelines for automated testing and deployment.
Example: Jenkins, GitLab CI.

11. Review and Iterate:
Regular Review:
Conduct regular code reviews and architecture evaluations.
Address issues and continuously improve the system.

