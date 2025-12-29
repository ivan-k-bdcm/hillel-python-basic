while True:
    first_number = float(input("Enter the first number: "))
    operator = input("Enter the operation: ")
    second_number = float(input("Enter the second number: "))

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = "Divide by zero error" if second_number == 0 else first_number / second_number
    else:
        result = f"{operator} is not a valid operator"

    print(result)

    next_calculation = input("Would you like to continue? (y/n): ").lower()

    if next_calculation == "y":
        continue
    else:
        break