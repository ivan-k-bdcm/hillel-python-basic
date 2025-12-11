minutes = int(input("Enter minutes:\n"))

hours = minutes // 60
minutes_left = minutes % 60

result = ""

if hours == 1:
    result += f"{hours} hour "
elif hours > 1:
    result += f"{hours} hours "

if minutes_left == 1:
    result += f"{minutes_left} minute"
elif minutes_left > 1:
    result += f"{minutes_left} minutes"

print(result)
