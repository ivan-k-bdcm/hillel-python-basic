class Car:
    def __init__(self, speed=0):
        self._speed = speed


    @property
    def speed(self):
        return self._speed


    def accelerate(self, acceleration):
        if acceleration <= 0:
            raise ValueError("Acceleration must be positive")
        self._speed = min(200, self._speed + acceleration)


    def brake(self, braking):
        if braking <= 0:
            raise ValueError("Braking must be positive")
        self._speed = max(0, self._speed - braking)


car1 = Car(0)

print(car1.speed)
car1.accelerate(300)
print(car1.speed)
car1.brake(300)
print(car1.speed)
