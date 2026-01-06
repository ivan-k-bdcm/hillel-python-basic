def common_elements():
    return {num for num in range(100) if num % 3 == 0 and num % 5 == 0}


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
