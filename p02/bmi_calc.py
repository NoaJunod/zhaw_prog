import math


def calc():
    weight = int(input("Please enter your weight in kg:"))
    height = int(input("Please enter your height in cm:"))

    bmi = weight / (height / 100)**2
    bsa = math.sqrt((height * weight) / 3600)

    print(f"Your BMI is {bmi} and your BSA is {bsa}")
    if bmi < 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("You are normal weight")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")
