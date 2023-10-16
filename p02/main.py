import age_calc
import bmi_calc
import blood_pressure
import med_dose_calc
import rock_paper_scissors
user_input = ''

while user_input != 'exit':
    user_input = input("Choose the program you want to run: \n"
                       "    0: Age calculator \n"
                       "    1: BMI/BSA calculator \n"
                       "    2: Blood Pressure categoriser \n"
                       "    3: Medicine dosage calculator \n"
                       "    4: Medical Rock Paper Scissors \n")

    if user_input == "0":
        age_calc.calc()
    elif user_input == "1":
        bmi_calc.calc()
    elif user_input == "2":
        blood_pressure.categorise()
    elif user_input == "3":
        med_dose_calc.calc()
    elif user_input == "4":
        rock_paper_scissors.play()