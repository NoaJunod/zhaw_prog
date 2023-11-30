import csv


# Exercise 2: Read Patient Data
def read_patient_records(filename):
    # TODO: Exercise 2 - Implement reading records from CSV file
    try:
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)

            records = {}
            for row in csv_reader:
                records[row['Patient ID']] = row
            return records
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Exercise 3: View Patient Records
def view_patient_records(records):
    # TODO: Exercise 3 - Implement displaying the patient records
    first_id = next(iter(records))
    keys = list(records[first_id].keys())
    print(f"{keys[0] : <10}{keys[1] : ^20}{keys[2] : ^15}{keys[3] : ^10}{keys[4] : >5}")
    for record in records:
        print(f"{records[record][keys[0]] : <10}{records[record][keys[1]] : ^20}{records[record][keys[2]] : ^15}{records[record][keys[3]] : ^10}{records[record][keys[4]] : >5}")


# Exercise 4: Add Patient Record
def add_patient_record(records):
    # TODO: Exercise 4 - Implement adding a new patient record
    valid_id = False
    patient_id = ''
    while not valid_id:
        patient_id = input('Patient ID: ')
        if patient_id in records:
            print(f'A patient with ID {patient_id} already exists.')
        else:
            valid_id = True
    name = input('Name: ')
    date_of_birth = input('Date of Birth: ')
    height = input('Height: ')
    weight = input('Weight: ')
    new_patient = {
        'Patient ID': patient_id,
        'Name': name,
        'Date of Birth': date_of_birth,
        'Height': height,
        'Weight': weight
    }
    records[patient_id] = new_patient


# Exercise 5: Update Patient Record
def update_patient_record(records):
    # TODO: Exercise 5 - Implement updating an existing patient record
    patient_id = input('Enter Patient ID you wish to update: ')
    if patient_id in records:
        patient = records[patient_id]
        print('Enter new values')
        patient['Name'] = input(f'Enter Name ({patient["Name"]}): ')
        patient['Date of Birth'] = input(f'Enter Date of Birth ({patient["Date of Birth"]}): ')
        patient['Height'] = input(f'Enter Height ({patient["Height"]}): ')
        patient['Weight'] = input(f'Enter Weight ({patient["Weight"]}): ')
    else:
        print(f'Patient {patient_id} does not exist.')


# Exercise 6: Delete Patient Record
def delete_patient_record(records):
    # TODO: Exercise 6 - Implement deleting a patient record
    patient_id = input('Enter Patient ID you wish to delete: ')
    if patient_id in records:
        records.pop(patient_id)
    else:
        print(f'Patient {patient_id} does not exist.')


# General: Writing Data Back to CSV
def write_patient_records(filename, records):
    # TODO: Implement writing records to CSV file (Refer to Exercises 4, 5, and 6)
    with open(filename, 'w', newline='') as file:
        first_id = next(iter(records))
        fieldnames = list(records[first_id].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow(records[r])


# Main function with the menu system
def main():
    records = read_patient_records("patient_records.csv")
    while True:
        print("\nPatient Records Management System")
        print("1. Add Patient Record")
        print("2. View Patient Records")
        print("3. Update Patient Record")
        print("4. Delete Patient Record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '2':
            view_patient_records(records)
        elif choice == '3':
            update_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '4':
            delete_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
