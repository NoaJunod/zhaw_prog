def check():
    user_input = input("Enter a list of heart-rates divided by commas (ex. '54, 32, 100, 87'): ")
    str_rates = user_input.split(",")

    rates = [int(x) for x in str_rates]
    counter = 0
    for r in rates:
        if 60 <= r <= 100:
            counter += 1

    print(f"{counter} heart-rates are within the normal range")
