def calculator(num1, num2, operation):
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція (додавання, віднімання, множення, ділення).
    :return: Результат операції.
    """
    result = 0

    ops = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'mul': lambda a, b: a * b,
        'div': lambda a, b: a / b if b != 0 else float('inf')
    }


    return ops[operation](num1, num2)

# Перевірка
assert calculator(5, 3, 'add') == 8
print("ОК")