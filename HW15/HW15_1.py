import math


class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError('Rectangle must have positive width and height')

        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return math.isclose(self.get_square(), other.get_square())

    def __add__(self, other) -> "Rectangle":
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area = self.get_square() + other.get_square()
        ratio = self.height / self.width
        new_width = math.sqrt(new_area / ratio)
        new_height = new_width * ratio
        return Rectangle(new_width, new_height)

    def __mul__(self, n: int) -> "Rectangle":
        k = math.sqrt(n)
        return Rectangle(self.width * k, self.height * k)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert math.isclose(r3.get_square(), 26), 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
