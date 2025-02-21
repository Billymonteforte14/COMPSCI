def add_numbers(a, b):
    return a + b
add_lambda = lambda a, b: a + b

print(f"Regular function result: {add_numbers(3, 5)}")
print(f"Lambda function result: {add_lambda(3, 5)}")