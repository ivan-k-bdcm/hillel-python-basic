def limit_calls(number):
    def decorator(func):
        counter = number

        def wrapper(*args, **kwargs):
            nonlocal counter
            if counter == 0:
                raise RuntimeError(
                    f"Function {func.__name__} can`t be called more than {number} times"
                )
            counter -= 1

            return func(*args, **kwargs)

        return wrapper

    return decorator


@limit_calls(2)
def ping():
    print("ping")


ping()
ping()
ping()  # RuntimeError
