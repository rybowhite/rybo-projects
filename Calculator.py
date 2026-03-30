import math
first = float(input("Enter first number: "))
second = float(input("Enter second number: ")) 
result = 0
operation = input("Enter the operation you want to perform (+, -, *, /, ^, sqrt): ")
if operation == "+":
    result = round(first + second, 2)
elif operation == "-":
    result = round(first - second, 2)
elif operation == "*":
    result = round(first * second, 2)   
elif operation == "/":
    result = first / second
elif operation == "^":
    result = first ** second
elif operation == "sqrt":
    result = math.sqrt(first)
else:
    print("Invalid operation")
print(f"The result is: {result}")   
