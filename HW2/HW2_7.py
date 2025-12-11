user_number = int(input("Enter 4-digit number:\n"))

digit, user_number = divmod(user_number, 1000)
print(digit)

digit, user_number = divmod(user_number, 100)
print(digit)

digit, user_number = divmod(user_number, 10)
print(digit)

print(user_number)
