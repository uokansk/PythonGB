a = с = 2
b = 3
print(a, id(a), b, id(b), с, id(с))
a = b + с
print(a, id(a), b, id(b), с, id(с))
