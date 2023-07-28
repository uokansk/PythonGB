data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')
print()

# И аналогичная операция в одну строку с распаковкой:

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')
