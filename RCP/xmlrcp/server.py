from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial
def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("XML-RPC Server listening on port 8000...")
server.register_function(factorial, "factorial")
server.serve_forever()
