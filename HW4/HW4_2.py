given_list = []

result = 0

for i in range(0, len(given_list), 2):
    result += given_list[i]

result = result * given_list[-1] if given_list else 0

print(result)