def common_elements():
    return set(num for num in range(100) if num % 3 == 0) & set(num for num in range(100) if num % 5 == 0)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
