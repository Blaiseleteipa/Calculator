a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == '+':
    result = a + b  
elif op == '-':
    result = a - b   
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print("Result:", result)
