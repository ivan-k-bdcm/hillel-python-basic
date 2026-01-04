def common_elements():
    int_division_by_3 = (num for num in range(100) if num % 3 == 0)
    int_division_by_5 = (num for num in range(100) if num % 5 == 0)

    return set(int_division_by_3) & set(int_division_by_5)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
