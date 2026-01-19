def is_even(number: int) -> bool:
    """
    Перевіряє, чи є число парним.

    Функція не використовує ділення або операції,
    пов'язані з ним (/, //, %, divmod).
    Працює для чисел будь-якого розміру.

    :param number: Ціле число
    :return: True, якщо число парне, False — якщо непарне
    """
    return not number & 1


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")