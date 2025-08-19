num_a = int(input('Enter first number: '))
num_b = int(input('Enter second number: '))
operation = input('Enter operation: ')

def calculator(num_a, num_b, operation):
    if operation == "+":
        print(num_a + num_b)
    elif operation == "-":
        print(num_a - num_b)
    elif operation == "*":
        print(num_a * num_b)
    elif operation == "/":
        print(num_a / num_b)
    else:
        print("Invalid operation")

calculator(num_a, num_b, operation)