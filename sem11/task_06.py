# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

from sem11.task_05 import Rectangle


class Difference(Rectangle):

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()


rect_1 = Rectangle(2, 3)
rect_2 = Rectangle(5)

print(f'Плошадь_1 = {rect_1.area()} > Плошади_2 = {rect_2.area()}, это: {rect_1.area() > rect_2.area()}')

print(f'Плошадь_1 = {rect_1.area()} < Плошади_2 = {rect_2.area()}, это: {rect_1.area() < rect_2.area()}')

print(f'Плошадь_1 = {rect_1.area()} = Плошади_2 = {rect_2.area()}, это: {rect_1.area() == rect_2.area()}')

print(f'Плошадь_1 = {rect_1.area()} <= Плошади_2 = {rect_2.area()}, это: {rect_1.area() <= rect_2.area()}')

print(f'Плошадь_1 = {rect_1.area()} >= Плошади_2 = {rect_2.area()}, это: {rect_1.area() >= rect_2.area()}')
