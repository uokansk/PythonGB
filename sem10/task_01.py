# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def len_circle(self):
        return pi * 2 * self.radius

    def area_circle(self):
        return pi * (self.radius ** 2)

    def volume(self):
        return pi * (self.radius ** 2) * self.height


r = float(input('Enter radius : '))
h = float(input('Enter height : '))
p = Circle(r, h)
print(f'Длина окружности = {p.len_circle() }, Площадь = {p.area_circle()}, Объём = {p.volume()}')
