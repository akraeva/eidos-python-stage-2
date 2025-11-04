# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 3. Кортежи | Тип данных - tupl

from sys import stdin

# pylint: disable=W0105

# 3.3 Задачи на усвоение кортежей + списков

# === Задача 1 ===
"""
    У вас есть два списка:
        Пользователь вводит количество n, а затем: Вводит n имен и n оценок.
        (реализуйте процесс приема данных с помощью циклов либо генераторов.)
        Создайте список кортежей, где каждый кортеж состоит из имени и
        соответствующего ему балла.
    """

# from sys import stdin


def m_3_3_1(data: str):
    lines = data.strip().split("\n")
    count = int(lines[0])
    names = [name for name in lines[1 : count + 1]]
    grades = [int(grade) for grade in lines[count + 1 :]]
    return list(zip(names, grades))


# print(m_3_3_1(stdin.read()))


# === Задача 2. ===
"""
    Программа принимает на вход 10 чисел в строку (реализуйте метод split()
    для правильной обработки чисел)
        1. Создайте кортеж, содержащий только уникальные элементы
           из этого списка, сохраняя их порядок.
        2. Определите количество встречающихся элементов и выведите
           это в формате кортежа (число, количество).
    """


def m_3_3_2(data: str):
    nums = list(map(int, data.strip().split()))
    counts = {key: nums.count(key) for key in dict.fromkeys(nums)}
    unique = tuple(counts.keys())
    result = tuple((key, value) for key, value in counts.items())
    return (
        f"Кортеж уникальных элементов: {unique}\n"
        f"Количество встречающихся элементов: {result}"
    )


# print(m_3_3_2(input()))


# === Задача 3. Модификация списка по индексу кортежа ===
"""
    Программа принимает на вход 10 чисел, а затем 3 индекса
    Увеличьте элементы собранного списка,
        чьи индексы указаны в кортеже, на 10%.
    Выведите измененный список.
    """


# from sys import stdin


def m_3_3_3(data: str):
    nums, ids = (list(map(int, line.split())) for line in data.strip().split("\n"))
    for i in set(ids):
        nums[i] = round(nums[i] * 1.1, 1)
    return f"Измененный список: {nums}"


# print(m_3_3_3(stdin.read()))


# === Задача 4. Обратная связь списков и кортежей ===
"""
    Дан кортеж:
        data = ("apple", "banana", "cherry", "apple",
                "date", "banana", "cherry", "fig")
        1. Преобразуйте кортеж в список, убрав все дубликаты.
        2. Отсортируйте список в алфавитном порядке.
        3. Преобразуйте отсортированный список обратно в кортеж.
    """


def m_3_3_4(data):
    result = sorted(set(data))
    return tuple(result)


# print(m_3_3_4(data))
