def cache(func):
    use_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in use_dict:
            return use_dict[key]
        else:
            result = func(*args, **kwargs)
            use_dict[key] = result
            return result




    return wrapper




@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
print(fibonacci(10))