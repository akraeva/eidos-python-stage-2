# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 4. Множества | Типы данных set и frozenset

from sys import stdin

# pylint: disable=W0105


# 4.1 Введение в множества | Тип данных set

# === Задача 1 ===

"""
    На ввод подаётся список с числами на одной строке через пробел.
    Преобразуйте каждый элемент введённого списка в тип данных int
    Выведите отсортированный по возрастанию список,
        содержащий только уникальные элементы.
    * Используйте преобразование списка в множество
    """


def m_4_1_1(data: str):
    nums = sorted(set(map(int, data.strip().split())))
    return nums


# print(m_4_1_1(input()))


# 4.2 Операции с множествами

# === Задача 1 ===
"""
    У вас есть множество languages = {"Python", "Java", "C++"}
    Удалите из множества элемент "С++", преобразуйте множество
    в список и выведите отсортированный по возрастанию список.
    """


def m_4_2_1(languages: set, element="C++"):
    languages.discard(element)
    return sorted(languages)


# print(m_4_2_1(languages))


# === Задача 2 ===
"""
    Даны два множества A и B. Найдите разность A - B.
    Преобразуйте полученное множество в список, отсортируйте его и выведите.
    """


def m_4_2_2(set_a: set, set_b: set):
    result = set_a - set_b
    return str(sorted(result))[1:-1]


# print(m_4_2_2(A, B))


# === Задача 3 ===
"""
    На ввод поддаются два списка list_1 и list_2.
    Преобразуйте списки в множества. Найдите их симметрическую разность.
    И преобразуйте полученное значение в отсортированный по возрастанию список.
    """

# from sys import stdin


def m_4_2_3(data: str):
    lists = [line.strip().split() for line in data.strip().split("\n")][:2]
    while len(lists) < 2:
        lists.append([])
    set_1, set_2 = map(set, lists)
    result = set_1 ^ set_2
    return sorted(result)


# print(m_4_2_3(stdin.read()))


# === Задача 4 ===
"""
    Даны два множества:
    Выведите:
        1.Общих друзей Анны и Бориса.
        2.Всех друзей Анны и Бориса без повторений.
        3.Друзей Анны, которые не дружат с Борисом.
    * Все выводы должны быть в формате отсортированого списка
    """


def m_4_2_4(anna: set, boris: set):
    common_friends = sorted(anna & boris)
    all_friends = sorted(anna | boris)
    anna_only = sorted(anna - boris)
    return f"{common_friends}\n{all_friends}\n{anna_only}"


# print(m_4_2_4(friends_anna, friends_boris))


# === Задача 5 ===
"""
    На ввод подаётся строка. Ваша задача:
        1.Создать множество уникальных слов в тексте
          (слова должны быть в нижнем регистре)
        2.Посчитайте и вывести количество уникальных слов
        3.Выведите слова в виде отсортированного списка
    """


def m_4_2_5(data: str):
    words = set(data.lower().strip().split())
    result = f"{len(words)}\n{sorted(words)}"
    return result


# print(m_4_2_5(input()))


# 4.3 Итерация по множествам и использование функций


# === Задача 1 ===
"""
    Дано множество numbers
    Создайте новое множество, содержащее только числа, большие 50
    Итоговое множество должно быть преобразовано в отсортированный
    список и выведено.
    """


def m_4_3_1(nums: set):
    result = {num for num in nums if num > 50}
    return sorted(result)


# print(m_4_3_1(numbers))


# === Задача 2 ===
"""
    Дано множество numbers
        1.Создайте новое множество even_numbers,
          содрежащее только чётные числа из numbers.
        2.Удаляет из исходного множества numbers все числа, кратные 5
        3.Выводит два преобразованных множества в отсортированные
          списки (сначала numbers, после even numbers)
    """


def m_4_3_2(nums: set):
    even_numbers = {num for num in nums if num % 2 == 0}
    to_remove = {num for num in nums if num % 5 == 0}
    nums -= to_remove
    return f"{sorted(nums)}\n{sorted(even_numbers)}"


# print(m_4_3_2(numbers))
