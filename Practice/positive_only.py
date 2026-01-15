def positive_only(func):
    def wrapper(*args, **kwargs):
        for x in args:
            if isinstance(x, (int, float)) and x <= 0:
                raise ValueError(
                    f"Function {func.__name__} can not operate negative numbers"
                )


        return func(*args, **kwargs)


    return wrapper


@positive_only
def multiply(a, b):
    return a * b


multiply(2, 3)  # працює
multiply(2, -1)
