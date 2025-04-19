import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take user input
try:
    number = int(input("Enter an integer: "))
    result = proxy.factorial(number)
    print(f"Factorial of {number} is {result}")
except Exception as e:
    print("Error:", e)
