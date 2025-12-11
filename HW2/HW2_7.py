user_number = int(input("Enter 4-digit number:\n"))

n, user_number = divmod(user_number,1000)

print(str(n) + "\n")

n, user_number = divmod(user_number,100)

print(str(n) + "\n")

n, user_number = divmod(user_number,10)

print(str(n) + "\n")

print(user_number)
