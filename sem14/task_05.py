# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.
import unittest


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


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(7)
        self.r3 = Rectangle(1, 9)
        self.r4 = Rectangle(1, 1)

    def test_create_rectangle(self):
        self.assertEqual(self.r1, Rectangle(3, 2))

    def test_perimeter(self):
        self.assertEqual(self.r2.perimeter(), 28)

    def test_area(self):
        self.assertEqual(self.r3.area(), 9)

    def test_not_eq(self):
        self.assertNotEquals(self.r1, self.r4)

    def test_sum(self):
        self.assertEqual(self.r2 + self.r3, Rectangle(8, 16))

    def test_sub(self):
        self.assertEqual(self.r1 - self.r4, Rectangle(2, 1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
