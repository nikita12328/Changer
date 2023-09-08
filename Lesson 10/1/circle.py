# Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    r = int(input("Введите радиус: "))
    circle1 = Circle(r)
    print(f"Площадь = {circle1.area()}")
    print(f"Длина = {circle1.perimeter()}")
