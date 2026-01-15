import time


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

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} executed in {end - start:.4f} seconds')
        return result


    return wrapper

@timer
def fibonacci_entry(n):
    return fibonacci(n)


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci_entry(6))
print(fibonacci_entry(100))