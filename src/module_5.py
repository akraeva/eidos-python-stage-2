# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 5. Словари | Тип данных dict

from sys import stdin


# pylint: disable=W0105


# 5.1 Введение в словари | dict()

# === Задача 1 ===

"""
    В ведомости есть всего один студент и тот решил сойти с курса и пойти
    на другую специальность. Да и было это 3 года назад. Поменяйте статус
    на обратный, добавьте 3 года к возрасту и выведите словарь на экран
    """


def m_5_1_1(pupil_john):
    pupil_john["age"] += 3
    pupil_john["is_student"] = False
    return pupil_john


# print(m_5_1_1(pupil_john))


# === Задача 2 ===

"""
    Дан словарь. student = {"name": "Alice", "age": 21}
    Добавьте в словарь новый элемент с ключом "city"
    и значением "Paris". Выведите словарь на экран
    """


def m_5_1_2(student):
    student = {"name": "Alice", "age": 21}
    student["city"] = "Paris"
    return student


# print(m_5_1_2())
