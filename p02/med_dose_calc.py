def calc():
    weight = int(input("Please enter your weight: "))
    dosage_per_weight = int(input("What dosage per kg do you need? (in mg)"))

    total_dosage = weight * dosage_per_weight
    total_capsules = total_dosage // 100
    deficit = total_dosage - (total_capsules * 100)

    print(f"Your total daily dosage is {total_dosage} mg")
    print(f"The amount of capsules you should take is {total_capsules}")
    print(f"The deficit is {deficit} mg")
