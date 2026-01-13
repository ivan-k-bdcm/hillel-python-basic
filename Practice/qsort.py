import random

def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr)-1)]
        less = [l for l in arr[1:] if l <= pivot]
        greater = [g for g in arr[1:] if g > pivot]
        return qsort(less) + [pivot] + qsort(greater)


print(qsort(list(random.choices(range(1000), k= 100))))