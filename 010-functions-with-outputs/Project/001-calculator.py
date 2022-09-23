def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

num1 = int(input("First number: "))
num2 = int(input("Second number: 10"))

for key, value in operations.items():
    print(key)

operation_symbol = input("Pick an operation symbol: ")

calcFunction = operations[operation_symbol]
answer = calcFunction(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

