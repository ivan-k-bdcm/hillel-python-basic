def flatten(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))  # рекурсивний виклик
        else:
            result.append(item)

    return result

assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
assert flatten([]) == []
assert flatten([1, [2, []], 3]) == [1, 2, 3]
print("OK")