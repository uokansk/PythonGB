# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, length, wide=None):
        self.length = length
        if wide is None:
            self.wide = length
        else:
            self.wide = wide

    def perimeter(self):
        return (self.wide + self.length) * 2

    def area(self):
        return self.wide * self.length


# long = float(input('Enter length : '))
# width = float(input('Enter wide : '))
p1 = Rectangle(2, 3)
p2 = Rectangle(2)
print(f'Периметр = {p1.perimeter()}, Площадь = {p1.area()}')
print(f'Периметр = {p2.perimeter()}, Площадь = {p2.area()}')
