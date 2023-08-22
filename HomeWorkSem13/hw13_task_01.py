
# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.


import csv


class MyException(Exception):
    pass


class InvalidNameError(MyException):
    def __init__(self, message="ФИО студента введено неверно. Оно должно содержать только буквы "
                               "и начинаться с заглавной буквы."):
        self.message = message
        super().__init__(self.message)


class SubjectError(MyException):
    def __init__(self, subject_name):
        self.message = f"Предмет '{subject_name}' не найден в файле CSV."
        super().__init__(self.message)


class ScoreError(MyException):
    def __init__(self, score, score_type="Оценка"):
        self.message = f"{score_type} '{score}' недействителен. Оценки должны быть от 2 до 5, " \
                       f"а результаты тестов от 0 до 100."
        super().__init__(self.message)


class Student:
    def __init__(self, family, name, surname, csv_file):
        if not name.istitle() or not name.replace(" ", "").isalpha() \
                or not family.istitle() or not family.replace(" ", "").isalpha() \
                or not surname.istitle() or not surname.replace(" ", "").isalpha():
            raise InvalidNameError()

        self.family = family
        self.name = name
        self.surname = surname

        with open(csv_file, 'r', newline='') as f:
            reader = csv.reader(f)
            self.subjects = {row[0]: {"grades": [], "test_scores": []} for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise SubjectError(subject)
        if grade < 2 or grade > 5:
            raise ScoreError(grade)
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise SubjectError(subject)
        if score < 0 or score > 100:
            raise ScoreError(score)
        self.subjects[subject]["test_scores"].append(score)

    def average_test_score(self):
        scores = [score for subj in self.subjects.values() for score in subj["test_scores"]]
        return sum(scores) / len(scores) if scores else 0

    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0


if __name__ == '__main__':
    stud_1 = Student('Ivanov', 'Ivan', 'Ivanovuch', 'subjects.csv')

    stud_1.add_grade('иностранный язык', 3)
    stud_1.add_grade('биология', 2)
    stud_1.add_test_score('биология', 78)
    print(stud_1.family, stud_1.name, stud_1.surname, stud_1.subjects)
    print(stud_1.average_grade())
    print(stud_1.average_test_score())
