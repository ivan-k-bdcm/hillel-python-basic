minutes = int(input("Enter minutes:\n"))
hour = minutes//60
minute = minutes%60
result = ""
if hour == 1:
    result += str(hour) + " hour "
elif hour > 1:
    result += str(hour) + " hours "


if minute == 1:
    result += str(minute) + " minute"
elif minute > 1:
    result += str(minute) + " minutes"

print(result)