# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
import abc


class Animal(abc.ABC):
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    @abc.abstractmethod
    def release_animal(self):
        pass


class Fish(Animal):
    def release_animal(self):
        print('рыба')


class Bird(Animal):
    def release_animal(self):
        print('птица')


class Cat(Animal):
    def release_animal(self):
        print('кот')


class AnimalFactory:
    @classmethod
    def create(cls, animal_type, name, color, size):
        animal_vendors = {
            "Fish": Fish,
            "Bird": Bird,
            "Cat": Cat,
        }
        return animal_vendors[animal_type](name, color, size)


if __name__ == "__main__":
    # fish = AnimalFactory.create('Fish')
    animal_1 = AnimalFactory.create('Fish', 'Flounder', 'orange', 10.2)
    animal_2 = AnimalFactory.create('Bird', 'Chichi', 'white', 82.3)
    animal_3 = AnimalFactory.create('Cat', 'Tom', 'black', 11)

    animal_1.release_animal()
    print(animal_1.name, animal_1.color, animal_1.size)

    animal_2.release_animal()
    print(animal_2.name, animal_2.color, animal_2.size)

    animal_3.release_animal()
    print(animal_3.name, animal_3.color, animal_3.size)
