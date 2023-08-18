# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        super(Fish, self).__init__(name, color, size)
        self.max_depth = max_depth

    def show_unique(self):
        print(self.max_depth)


class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, areal: str):
        super(Bird, self).__init__(name, color, size)
        self.areal = areal

    def show_unique(self):
        print(self.areal)


class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        super(Cat, self).__init__(name, color, size)
        self.hairy = hairy

    def show_unique(self):
        print(self.hairy)


if __name__ == "__main__":
    fish = Fish('Flounder', 'orange', 10.2, 15.0)
    bird = Bird('Chichi', 'white', 82.3, 'forest')
    cat = Cat('Tom', 'black', 11, True)

    animals = (fish, bird, cat)
    for animal in animals:
        animal.show_unique()
