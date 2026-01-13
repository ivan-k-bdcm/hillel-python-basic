def max_r(arr: list) -> list:
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max_r([2, 2, 1, 0, 5, 5, -2, 8, 1, 0, 5, -1]))