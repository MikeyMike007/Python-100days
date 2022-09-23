height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight = float(weight)
height = float(height)

BMI = weight / (height ** 2)

# round() rounds a fraction to a whole number
print(round(BMI))

