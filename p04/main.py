def analyze_patient(patient):
    print(f"Patient Name: {patient['Patient Name']}")
    print(analyze_heart_rate_age(patient['Heart Rate'], patient['Age']))
    print(analyze_blood_pressure(patient['Systolic Blood Pressure'], patient['Diastolic Blood Pressure']))


def analyze_heart_rate_age(heart_rate, age):
    state = ""
    if age < 1:
        if heart_rate < 120:
            state = "low"
        elif heart_rate < 141:
            state = "normal"
        else:
            state = "high"
    elif age < 4:
        if heart_rate < 100:
            state = "low"
        elif heart_rate < 121:
            state = "normal"
        else:
            state = "high"
    elif age < 18:
        if heart_rate < 80:
            state = "low"
        elif heart_rate < 101:
            state = "normal"
        else:
            state = "high"
    else:
        if heart_rate < 60:
            state = "low"
        elif heart_rate < 81:
            state = "normal"
        else:
            state = "high"
    return f"Heart Rate is {state} for the age {age}"


def analyze_blood_pressure(sys_pres, dia_pres):
    if sys_pres == 0 and dia_pres == 0:
        return "Patient is dead"
    elif (sys_pres > 180 and dia_pres > 120) or (sys_pres > 180 or dia_pres > 120):
        return "Patient is in a Hypertensive crisis"
    elif sys_pres >= 140 or dia_pres >= 90:
        return "Patient is in Hypertension Stage 2"
    elif 130 <= sys_pres <= 139 or 80 <= dia_pres <= 89:
        return "Patient is in Hypertension Stage 1"
    elif 120 <= sys_pres <= 129 and dia_pres < 80:
        return "Patients pressure is elevated"
    elif sys_pres < 120 and dia_pres < 80:
        return "Patients pressure is normal"


def get_patient_data():
    print("Enter the patients data:")
    name = input("Patient Name: ")
    ahv = input("AHV Number: ")
    age = int(input("Age: "))
    temperature = float(input("Temperature (in Celsius): "))
    heart_rate = int(input("Heart Rate (in bpm): "))
    systolic_blood_pressure = int(input("Systolic Blood Pressure (in mmHg): "))
    diastolic_blood_pressure = int(input("Diastolic Blood Pressure (in mmHg): "))
    patient = {
        "Patient Name": name,
        "AHV Number": ahv,
        "Age": age,
        "Temperature": temperature,
        "Heart Rate": heart_rate,
        "Systolic Blood Pressure": systolic_blood_pressure,
        "Diastolic Blood Pressure": diastolic_blood_pressure
    }
    return patient


def mass_data_entry():
    patients = []
    patients.append(get_patient_data())
    user_input = input("Enter another patient? (yes/no)")
    while user_input == "yes":
        patients.append(get_patient_data())
        user_input = input("Enter another patient? (yes/no)")
    else:
        return index_patient_data(patients)


def index_patient_data(patient_list):
    indexed_patients = {}
    for p in patient_list:
        if p['AHV Number']:
            indexed_patients[p['AHV Number']] = p
    return indexed_patients


def retrieve_and_analyze_patient_data(i_patients, ahv):
    if ahv in i_patients:
        patient = i_patients[ahv]
        analyze_patient(patient)
    else:
        print(f"No Patient with AHV Number {ahv} has been found!")


def handle_lookup_inputs(i_patients):
    user_input = input("Enter AHV Number (or type 'quit' to exit):")
    while user_input != "quit":
        retrieve_and_analyze_patient_data(i_patients, user_input)
        user_input = input("Enter AHV Number (or type 'quit' to exit):")


def main():
    print("Starting Program...")
    i_p = mass_data_entry()
    handle_lookup_inputs(i_p)


if __name__ == "__main__":
    main()
