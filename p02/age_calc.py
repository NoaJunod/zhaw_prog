from datetime import datetime


def calc():
    current_year = datetime.now().year
    age_input = input("Please Enter your Age:")
    if age_input.isnumeric():
        age = int(age_input)
        birth_year = current_year - age
        hundred_year = birth_year + 100
        print(f"You will be 100 years old in {hundred_year} and you were born in {birth_year}")
    else:
        print("Input is invalid")
