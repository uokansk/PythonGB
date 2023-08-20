# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyStr(str):
    """
    This documentation
    """
    def __new__(cls, text, creator):
        """
        This documentation new
        """
        print('New str')
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        """
        This doc is help
        """
        return f'{super().__str__()} created by: {self.creator} at {self.time}'


example = MyStr('text', 'name')
example2 = MyStr('text2', 'name2')
print(example)
print(example2)

print(help(MyStr.__str__.__doc__))
