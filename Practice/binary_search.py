import random

def binary_search(aim):
    arr = range(0, 1000, 25)
    print(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]
        if guess == aim:
            return mid
        elif guess > aim:
            high = mid - 1
        else:
            low = mid + 1

    return None





print(binary_search(36))