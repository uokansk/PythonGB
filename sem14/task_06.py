# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

import pytest
from sem13.task_05 import Project, User


@pytest.fixture
def new_set():
    user_set = {User('Masha', 13, 6),
                User('Konstantin', 12, 2),
                User('Alexandr', 14, 4)}
    return user_set


def test_entrance(new_set):
    project = Project()
    result = project.users_from_json('users.json')
    assert result == new_set()


if __name__ == '__main__':
    pytest.main(['-vv'])