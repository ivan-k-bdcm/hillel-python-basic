def sum_r(arr: list) -> int | float:
    if not arr:
        return 0
    else:
        return arr[0] + sum_r(arr[1:])



print(sum_r([1,2,3,4,5,6,7,8,9,11]))