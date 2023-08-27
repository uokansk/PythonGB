# 📌 Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.
import csv
import logging
import argparse

logging.basicConfig(filename='e_student.log.', encoding='utf-8', level=logging.ERROR)


def parse():
    parser = argparse.ArgumentParser(prog='Student',
                                     description='Вводим оценки и результаты тестов студентам')

    parser.add_argument('-f', '--family', help='Фамилия студента')
    parser.add_argument('-n', '--name', help='Имя студента')
    parser.add_argument('-s', '--surname', help='Отчество студента')
    parser.add_argument('-с', '--csv_file', help='Список предметов')
    args = parser.parse_args()
    stud_1 = Student(args.family, args.name, args.surname, args.csv_file)
    print(stud_1.add_grade('математика', 5))

    # return Student(f'{args.family} {args.name} {args.surname} {args.csv_file}')


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
        try:
            self.family = family
            self.name = name
            self.surname = surname
            self.subjects = self.load_subjects(csv_file)

            if not name.istitle() or not name.replace(" ", "").isalpha() \
                    or not family.istitle() or not family.replace(" ", "").isalpha() \
                    or not surname.istitle() or not surname.replace(" ", "").isalpha():
                raise InvalidNameError()
        except InvalidNameError:
            logging.error(f'ФИО студента введено неверно {family} {name} {surname}')

    def load_subjects(self, csv_file):
        with open(csv_file, 'r', newline='') as f:
            reader = csv.reader(f)
            return next(reader)
            # self.subjects = {row[0]: {"grades": [], "test_scores": []} for row in reader}

    def add_grade(self, subject, grade):
        try:
            if subject not in self.subjects:
                raise SubjectError(subject)
            if grade < 2 or grade > 5:
                raise ScoreError(grade)
        except ScoreError:
            logging.error(f' {subject} Предмета нет в списке или такой оценки нет {grade} ')
            self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        try:
            if subject not in self.subjects:
                raise SubjectError(subject)
            if score < 0 or score > 100:
                raise ScoreError(score)
        except ScoreError:
            logging.error(f' {subject} Предмета нет в списке или такой оценки нет {score} ')
            self.subjects[subject]["test_scores"].append(score)

    def average_test_score(self):
        scores = [score for subj in self.subjects.values() for score in subj["test_scores"]]
        return sum(scores) / len(scores) if scores else 0

    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0


if __name__ == '__main__':
    # stud_1 = Student('Ivanov', 'Ivan', 'Ivanovuch', 'subjects.csv')
    # stud_1.add_grade('иностранный язык', 6)
    # stud_1.add_grade('биолог', 2)
    # stud_1.add_test_score('биология', 78)
    # print(stud_1.average_grade())
    print(parse())
