def categorise():
    sys_pres = int(input("Please enter your systolic blood pressure value:"))
    dia_pres = int(input("Please enter your diastolic blood pressure value:"))

    if sys_pres == 0 and dia_pres == 0:
        print("You are dead")
    elif (sys_pres > 180 and dia_pres > 120) or (sys_pres > 180 or dia_pres > 120):
        print("You are in a Hypertensive crisis")
    elif sys_pres >= 140 or dia_pres >= 90:
        print("You are in Hypertension Stage 2")
    elif 130 <= sys_pres <= 139 or 80 <= dia_pres <= 89:
        print("You are in Hypertension Stage 1")
    elif 120 <= sys_pres <= 129 and dia_pres < 80:
        print("Your blood pressure is elevated")
    elif sys_pres < 120 and dia_pres < 80:
        print("Your blood pressure is normal")
