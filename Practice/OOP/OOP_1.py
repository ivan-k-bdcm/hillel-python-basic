"""
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age




user1 = User("Ivan", 26)
user2 = User("Oleg", 20)

print(user1.name)
print(user2.age)
"""

"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'Woof! Мене звати {self.name}')


dog = Dog("Rex", 3)
dog.bark()
"""


class Car:
    def __init__(self, brand, speed = 0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, acceleration: int | float) -> int | float:
        if acceleration < 0:
            print(f'Acceleration must be positive')
            return self.speed

        self.speed += acceleration

        return self.speed

    def brake(self, braking: int | float) -> int | float:
        self.speed = max(0, self.speed - braking)

        return self.speed


car1 = Car("Toyota")
car2 = Car("Honda")

car1.accelerate(50)
car2.accelerate(30)

print(car1.speed)  # 50
print(car2.speed)  # 30

car1.brake(20)
print(car1.speed)  # 30
print(car2.speed)
