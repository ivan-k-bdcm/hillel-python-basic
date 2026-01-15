import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} executed in {end - start:.4f} seconds')
        return result


    return wrapper








@timer
def slow_sum(n):
    return sum(range(n))


slow_sum(100000)

slow_sum(100000)

slow_sum(100000)