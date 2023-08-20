# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, side_a, side_b=None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def perimeter(self):
        return (self.side_b + self.side_a) * 2

    def area(self):
        return self.side_b * self.side_a


# long = float(input('Enter length : '))
# width = float(input('Enter wide : '))
# p1 = Rectangle(2.3, 3.5)
# p2 = Rectangle(2)
# print(f'Периметр = {p1.perimeter()}, Площадь = {p1.area()}')
# print(f'Периметр = {p2.perimeter()}, Площадь = {p2.area()}')
