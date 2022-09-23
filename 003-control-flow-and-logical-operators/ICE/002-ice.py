# Estimates your BMI and provides a comment

height = float(input("What is your height: "))
weight = float(input("What is your weight: "))

bmi = weight / (height ** 2)
bmi = round(bmi, 2)

if bmi < 18.5:
    print("Your BMI is " + str(bmi) + ", you are underweight")
elif bmi >= 18.5 and bmi < 25:
     print("Your BMI is " + str(bmi) + " , you have a normal weight")
elif bmi >= 25 and bmi < 30:
     print("Your BMI is " + str(bmi) + " , you are slightly overweight")
elif bmi >= 30 and bmi < 35:
     print("Your BMI is " + str(bmi) + " , you are obese")
else:
    print("Your BMI is " + str(bmi) + " , you are clinically obese")


