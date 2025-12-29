number = int(input("Enter time in seconds(0 - 8640000): "))

if 0 <= number <= 8640000:

    seconds_in_day = 24 * 60 * 60
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days, remains = divmod(number, seconds_in_day)
    hours, remains = divmod(remains, seconds_in_hour)
    minutes, seconds = divmod(remains, seconds_in_minute)

    if days == 1:
        day_word = "day"
    else:
        day_word = "days"
    result = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
else:
    result = "Time must be in range 0 - 8640000"
print(result)