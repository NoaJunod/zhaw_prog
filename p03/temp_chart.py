def chart():
    days = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']
    user_input = input("Enter a list of 7 temperatures divided by commas (ex. '36.3, 35.7, 41.4, 40.0, 39.6, 38.9, 39.3'): ")
    str_temps = user_input.split(",")

    temps = [float(x) for x in str_temps]

    avg_temp = sum(temps) / len(temps)
    day_above_avg = []
    for i in range(0, 7):
        if temps[i] > avg_temp:
            day_above_avg.append(days[i])

    print(f"The average body temperature of this week is: {avg_temp:.2f}°C")
    days_str = ", ".join(day_above_avg)
    print(f"The days the body temperature were above average were: {days_str}.")
