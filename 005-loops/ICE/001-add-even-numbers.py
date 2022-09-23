totalSum = 0

for number in range(1,100 + 1):
    if number % 2 == 0:
        totalSum += number

print(f"Sum of even numbers is {totalSum}")