# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

import sys


class Rectangle:
    __slots__ = ('__side_a', '__side_b')

    def __init__(self, side_a, side_b=None):
        self.__side_a = side_a
        if side_b is None:
            self.__side_b = side_a
        else:
            self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        if value > 0:
            self.__side_a = value
        else:
            raise ValueError('Отрицательные и нулевые не допустимы')

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        if value > 0:
            self.__side_b = value
        else:
            raise ValueError('Отрицательные и нулевые не допустимы')

    def perimeter(self):
        return (self.__side_b + self.__side_a) * 2

    def area(self):
        return self.__side_b * self.__side_a

    def __add__(self, other):
        sum_of_perimeter = self.perimeter() + other.perimeter()
        side_a = self.__side_a + other.side_a
        side_b = sum_of_perimeter / 2 - side_a
        return Rectangle(side_a, side_b)

    def __sub__(self, other):
        # if self.perimeter() < other.perimeter():
        #     self, other = other, self
        diff = abs(self.perimeter() - other.perimeter())
        side_a = abs(self.__side_a - other.side_a)
        side_b = diff / 2 - side_a
        return Rectangle(side_a, side_b)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        if self.__side_a == self.__side_b:
            return f'Square with side {self.__side_a}'
        else:
            return f'Square with side {self.__side_a} and {self.__side_b}'

    def __repr__(self):
        return f'Rectangle ({self.__side_a}, {self.__side_b})'


if __name__ == '__main__':
    rect_1 = Rectangle(5, 10)
    rect_2 = Rectangle(10, 20)
    # rect_1.side_a = 7
    # print(rect_1.side_a)
    # rect_3 = rect_1 + rect_2
    # rect_4 = rect_2 - rect_1
    #
    # print(f'{rect_1.side_a = }, {rect_1.side_b = }, {rect_1.perimeter()}')
    # print(f'{rect_3.side_a = }, {rect_3.side_b = }, {rect_3.perimeter()}')
    # print(f'{rect_4.side_a = }, {rect_4.side_b = }, {rect_4.perimeter()}')

    print(sys.getsizeof(rect_1))
