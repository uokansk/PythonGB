# f = open('task_01_f.txt', 'r', encoding='utf-8', errors='replace')
# print(f.read())
# f.close()


with open('task_01_f.txt', 'r', encoding='utf-8') as f:
    for line in f:
        str(f)
        a = line.split('|')

    print(a, end='')
