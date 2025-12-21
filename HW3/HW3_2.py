numbers = [12, 3, 4, 10, 8]

if len(numbers) > 1:
    rotated_numbers = [numbers[-1]] + numbers[:-1]
else:
    rotated_numbers = numbers

print(rotated_numbers)
