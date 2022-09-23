def isPrime(number):
    isNumberPrime = True
    for num in range(2,number):
        if (number % num == 0):
            isNumberPrime = False
            break
    return isNumberPrime






n = int(input("Check this number: "))

if isPrime(n):
    print(f"Number {n} is a prime")
else:
    print(f"Number {n} is not a prime")


