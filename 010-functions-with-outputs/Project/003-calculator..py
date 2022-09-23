def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

savedResults = []

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

for key in operations:
    print(key)

operation_symbol = input("Choose operation: ")
operation = operations[operation_symbol]
result = operation(n1, n2)
savedResults.append(result)
print(f"{n1} {operation_symbol} {n2} = {result}")

calculateFurther = True

while calculateFurther:
    operation_symbol = input("Pick another operation if you want to continue (n to break): ")
    if operation_symbol == "n":
        calculateFurther = False
        break
    n3 = int(input("Next number: "))
    operation = operations[operation_symbol]
    result = operation(savedResults[-1], n3)
    print(f"{savedResults[-1]} {operation_symbol} {n3} = {result}")
    savedResults.append(result)
    