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
