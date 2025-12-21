import random

rand_number_list = []

for amount in range(random.randint(3, 10)):
    rand_number_list.append(random.randint(1, 100))

print(rand_number_list)

result_list = [rand_number_list[0]] + [rand_number_list[2]] + [rand_number_list[-2]]

print(result_list)
