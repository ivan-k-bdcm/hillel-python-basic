def idxSmallest(arr: list) -> int:
    smallest = arr[0]
    smallest_idx = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
        else:
            continue
    return smallest_idx



def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest = idxSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr



print(selection_sort([2, 2, 1, 0, 5, 5, -2, 8, 1, 0, 5, -1]))