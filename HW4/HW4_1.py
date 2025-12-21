given_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

result = []
zero_count = 0

for number in given_list:
    if number == 0:
        zero_count += 1
    else:
        result.append(number)

result.extend([0] * zero_count)

print(result)
