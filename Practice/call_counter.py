def call_counter(func):
    counter = 0


    def wrapper():
        nonlocal counter
        counter += 1
        print(counter)
        return (func())


    return wrapper


@call_counter
def say_hello():
    print('Hello World!')



say_hello()
say_hello()
say_hello()
say_hello()