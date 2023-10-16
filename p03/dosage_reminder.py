def remind():
    frequency = int(input("Enter the frequency you want to take your dosage in: "))
    for i in range(0, 24):
        if i % frequency == 0:
            print(f"Hour {i}: Take your dosage")
        else:
            print(f"Hour {i}:")
