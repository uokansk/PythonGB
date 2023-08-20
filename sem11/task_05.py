# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.


from sem10.task_02 import Rectangle


class RectanglePro(Rectangle):

    def __add__(self, other):
        sum_of_perimeter = self.perimeter() + other.perimeter()
        side_a = self.side_a + other.side_a
        side_b = sum_of_perimeter / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __sub__(self, other):
        # if self.perimeter() < other.perimeter():
        #     self, other = other, self
        diff = abs(self.perimeter() - other.perimeter())
        side_a = abs(self.side_a - other.side_a)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)


# p1 = Rectangle(2, 3)
# p2 = Rectangle(5)
# print(f'Периметр = {p1.perimeter()}, Площадь = {p1.area()}')
# print(f'Периметр = {p2.perimeter()}, Площадь = {p2.area()}')

rect_1 = RectanglePro(2, 3)
rect_2 = RectanglePro(5)


print(rect_1.perimeter())
print(rect_2.perimeter())
rect_sum = rect_1 + rect_2
print(rect_sum.perimeter())
print(rect_sum.side_a, rect_sum.side_b)
rect_dif = rect_1 - rect_2
print(rect_dif.perimeter())
print(rect_dif.side_a, rect_dif.side_b)
