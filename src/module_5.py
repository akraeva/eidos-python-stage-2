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


def m_5_1_1(pupil):
    pupil["age"] += 3
    pupil["is_student"] = False
    return pupil


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


# print(m_5_1_2(student))


# 5.2 Методы изменения словарей | del() pop() popitem() clear()

# === Задача 1 ===

"""
    Дан словарь
    Добавление элементов:
        - Добавьте 5 яблок в инвентарь.
        - Увеличьте количество бананов на 2.
        - Выведите словарь на экран
    Удаление элементов:
        - Теперь удалите все апельсины из инвентаря.
        - Удалите один виноград.
        - Выведите словарь на экран
    Обновление значений:
        - Обновите количество арбузов до 4 (если арбуза нет — добавьте его с количеством 4).
        - Выведите словарь на экран
    Проверка наличия элемента:
        - Проверьте, есть ли в инвентаре "melon". Если есть — выведите его количество.
        - Выведите словарь на экран
    Метод popitem():
        - Используйте метод popitem() для удаления случайного элемента из словаря и выведите этот элемент.
        - Выведите словарь на экран
    Очистка инвентаря:
        - Очистите весь инвентарь с помощью метода clear().
        - Выведите словарь на экран
    """


def m_5_2_1(inventory: dict):
    result = []
    inventory["apple"] = inventory.get("apple", 0) + 5
    inventory["banana"] = inventory.get("banana", 0) + 2
    result.append(f"После добавления элементов: {inventory}")

    if "orange" in inventory:
        del inventory["orange"]
    if "grapes" in inventory and inventory["grapes"] > 0:
        inventory["grapes"] -= 1
    result.append(f"После удаления элементов: {inventory}")

    inventory["watermelon"] = 4
    result.append(f"После обновления значений: {inventory}")
    result.append(
        f"Количество арбузов (melon): {inventory['melon'] if "melon" in inventory else 0}"
    )
    result.append(f"После проверки наличия элемента: {inventory}")

    element = inventory.popitem()
    result.append(f"Удаленный элемент: {element}")
    result.append(f"После использования popitem(): {inventory}")

    inventory.clear()
    result.append(f"После очистки инвентаря: {inventory}")
    return "\n".join(result)


# print(m_5_2_1(inventory))
