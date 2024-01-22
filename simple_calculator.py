#!/usr/bin/python3

# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# User input
number1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
number2 = float(input("Enter the second number: "))

# Operation selection
if operator == "+":
    result = add(number1, number2)
elif operator == "-":
    result = subtract(number1, number2)
elif operator == "*":
    result = multiply(number1, number2)
elif operator == "/":
    result = divide(number1, number2)
else:
    result = "Invalid operator"

# Output result
print("Result:", result)

# Additional information with GitHub link
print("For more information, visit: https://github.com/zaedstudioshpkentang")