# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух
# других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами
# не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# a, b, c = int(input('Input sides of a triangle')) не получилось

a = int(input('Input side A of triangle: '))
b = int(input('Input side B of triangle: '))
c = int(input('Input side C of triangle: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Equilateral triangle')
    elif a == b or a == c or c == b:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')
else:
    print('It is not a triangle')
