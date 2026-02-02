class Counter:
    """Counter with minimum value and maximum value"""
    def __init__(self, current: int=1, min_value: int=0, max_value: int=10) -> None:
        """
        Initialize the counter.

        :param current: Initial counter value
        :param min_value: Minimum allowed value
        :param max_value: Maximum allowed value
        """
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        """
        Set the current counter value.

        :param start: New current value
        """
        self.current = start

    def set_max(self, max_max: int) -> None:
        """
        Set the maximum allowed value.

        :param max_max: New maximum allowed value
        """
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """
        Set the minimum allowed value.

        :param min_min: New maximum allowed value
        """
        self.min_value = min_min

    def step_up(self) -> None:
        """
        Increase the counter by 1.

        :raises ValueError: If maximum value is reached
        """
        if self.current == self.max_value:
            raise ValueError('Error: Max value reached')
        self.current += 1

    def step_down(self) -> None:
        """
        Decrease the counter by 1.

        :raises ValueError: If minimum value is reached
        """
        if self.current == self.min_value:
            raise ValueError('Error: Min value reached')
        self.current -= 1

    def get_current(self) -> int:
        """
        Get the current counter value.

        :return: Current value
        """
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
