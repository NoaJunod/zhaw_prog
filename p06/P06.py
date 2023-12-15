import random
import psycopg2
import re


def count_patients():
    # Implement the query and return an integer
    # Example: return 10
    conn = psycopg2.connect(
        database="starwars_medical", user='postgres', password='rootroot', host='127.0.0.1', port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(1) FROM patients")

    data = cursor.fetchone()[0]

    count = int(data)
    conn.close()
    return count


def get_patients_by_blood_group(blood_group):
    # Implement the query and return a list
    # Example: return [{'name': 'Luke Skywalker', 'age': 53, 'planet': 'Tatooine'}]
    conn = psycopg2.connect(
        database="starwars_medical", user='postgres', password='rootroot', host='127.0.0.1', port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT p.name, p.age, p.planet"
                   " FROM patients AS p"
                   " FULL OUTER JOIN blood_groups as b"
                   " ON p.blood_group_id=b.id"
                   " WHERE b.type=%s", (blood_group, ))

    data = cursor.fetchall()
    patient_list = []
    for patient in data:
        if patient[0] is None:
            break
        patient_list.append({'name': patient[0], 'age': int(patient[1]), 'planet': patient[2]})
    conn.close()
    return patient_list


def insert_patient(name, age, planet, blood_group):
    # Implement the query and return the ID of the newly created patient
    # Example: return 1234
    conn = psycopg2.connect(
        database="starwars_medical", user='postgres', password='rootroot', host='127.0.0.1', port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, planet, blood_group_id)"
                   " VALUES (%s, %s, %s, (SELECT id FROM blood_groups WHERE type=%s))"
                   " RETURNING id;",
                   (name, age, planet, blood_group))

    data = cursor.fetchone()[0]

    conn.commit()
    patient_id = int(data)
    conn.close()
    return patient_id


def verify_count(result):
    if isinstance(result, int):
        print("Success: Count is an integer, as expected.")
    else:
        print("Error: Count should be an integer.")


def verify_patient_list(result):
    if isinstance(result, list) and all(isinstance(item, dict) for item in result):
        print("Success: Patient list is a list of dictionaries, as expected.")
    else:
        print("Error: Patient list should be a list of dictionaries.")


def verify_insertion(result):
    if isinstance(result, int):
        print("Success: Inserted patient ID is an integer, as expected.")
    else:
        print("Error: Inserted patient ID should be an integer.")


def main():
    # !!! DO NOT MODIFY THIS FUNCTION !!!
    # ALL YOUR WORK SHOULD BE DONE IN THE 3 FUNCTIONS ABOVE

    # Possible new patients
    potential_new_patients = [
        {'name': 'Obi-Wan Kenobi', 'age': 57, 'planet': 'Stewjon', 'blood_group': 'A+'},
        {'name': 'Anakin Skywalker', 'age': 45, 'planet': 'Tatooine', 'blood_group': 'B+'},
        {'name': 'Padme Amidala', 'age': 46, 'planet': 'Naboo', 'blood_group': 'AB+'},
        {'name': 'Mace Windu', 'age': 64, 'planet': 'Haruun Kal', 'blood_group': 'O-'},
        {'name': 'Qui-Gon Jinn', 'age': 60, 'planet': 'Coruscant', 'blood_group': 'A-'}
    ]

    chosen_patient = random.choice(potential_new_patients)

    # Call and verify the functions
    count_result = count_patients()
    verify_count(count_result)

    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    chosen_blood_group = random.choice(blood_groups)
    patient_list_result = get_patients_by_blood_group(chosen_blood_group)
    verify_patient_list(patient_list_result)

    insert_result = insert_patient(**chosen_patient)
    verify_insertion(insert_result)


if __name__ == '__main__':
    main()
