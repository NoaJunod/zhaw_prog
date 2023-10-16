import pulse_check
import dosage_reminder
import temp_chart
import blood_vessel_overlap
user_input = ''

while user_input != 'exit':
    user_input = input("Choose the program you want to run: \n"
                       "    0: Pulse Check \n"
                       "    1: Dosage Reminder \n"
                       "    2: Temperature Chart \n"
                       "    3: Blood Vessel Overlap \n")

    if user_input == "0":
        pulse_check.check()
    elif user_input == "1":
        dosage_reminder.remind()
    elif user_input == "2":
        temp_chart.chart()
    elif user_input == "3":
        blood_vessel_overlap.examine()
