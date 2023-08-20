import sys


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError('Negative and zero are not allowed')


class Rectangle:
    side_a = Descriptor()
    side_b = Descriptor()

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

    def __add__(self, other):
        sum_of_perimeter = self.perimeter() + other.perimeter()
        side_a = self.side_a + other.side_a
        side_b = sum_of_perimeter / 2 - side_a
        return Rectangle(side_a, side_b)

    def __sub__(self, other):
        # if self.perimeter() < other.perimeter():
        #     self, other = other, self
        diff = abs(self.perimeter() - other.perimeter())
        side_a = abs(self.side_a - other.side_a)
        side_b = diff / 2 - side_a
        return Rectangle(side_a, side_b)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        if self.side_a == self.side_b:
            return f'Square with side {self.side_a}'
        else:
            return f'Square with side {self.side_a} and {self.side_b}'

    def __repr__(self):
        return f'Rectangle ({self.side_a}, {self.side_b})'


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
