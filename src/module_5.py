# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 5. Словари | Тип данных dict

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
        - Обновите количество арбузов до 4
          (если арбуза нет — добавьте его с количеством 4).
        - Выведите словарь на экран
    Проверка наличия элемента:
        - Проверьте, есть ли в инвентаре "melon".
          Если есть — выведите его количество.
        - Выведите словарь на экран
    Метод popitem():
        - Используйте метод popitem() для удаления случайного
          элемента из словаря и выведите этот элемент.
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
        f"Количество арбузов (melon): {inventory['melon'] if 'melon' in inventory else 0}"
    )
    result.append(f"После проверки наличия элемента: {inventory}")

    element = inventory.popitem()
    result.append(f"Удаленный элемент: {element}")
    result.append(f"После использования popitem(): {inventory}")

    inventory.clear()
    result.append(f"После очистки инвентаря: {inventory}")
    return "\n".join(result)


# print(m_5_2_1(inventory))


# 5.3 Основные методы словарей | keys() values() items() get()


# === Задача 1. Использование метода values() ===
"""
    Используйте словарь из предыдущей задачи:
        - Получите все значения из словаря с помощью метода values().
        - Выведите все значения на экран.
    """


def m_5_3_1(data: dict):
    return data.values()


# print(m_5_3_1(inventory))


# === Задача 2 ===
"""
    У вас есть следующий словарь:
        - Используйте метод keys() для получения всех ключей словаря inventory.
        - Выведите все ключи на экран.
    """


def m_5_3_2(data: dict):
    return data.keys()


# print(m_5_3_2(inventory))


# === Задача 3. Использование метода items() ===
"""
    Используйте словарь:
        - Используйте метод items() для получения всех пар "ключ-значение".
        - Пройдитесь по этим парам и выведите их в формате: "ключ: значение".
    """


def m_5_3_3(data: dict):
    result = [f"{key}: {value}" for key, value in data.items()]
    return "\n".join(result)


# print(m_5_3_3(inventory))


# === Задача 4. Использование метода get() ===
"""
    Используйте словарь:
        - Используйте метод get() для получения значения по ключу "banana".
        - Используйте метод get() для получения значения по ключу "pear".
          В случае отсутствия ключа верните строку "Not found".
        - Выведите оба результата на экран.
    """


def m_5_3_4(data: dict, queries=("banana", "pear")):
    result = [data.get(query, "Not found") for query in queries]
    return "\n".join(map(str, result))


# print(m_5_3_4(inventory))


# 5.4 Словари, как значения других словарей. Вложенные словари


# === Задача 1 Поиск максимального значения во вложенных словарях ===
"""
    Дан словарь: Найдите имя пользователя
    с максимальным значением поля "score".
    """


def m_5_4_1(data: dict, field="score"):
    max_data = max(data.values(), key=lambda user: user[field])
    return max_data["name"]


# print(m_5_4_1(data))


# === Задача 2 ===
"""
    Даны два вложенных словаря: Объедините эти словари так, чтобы значения
    пересекающихся ключей также были объединены. Если ключ повторяется,
    берется значение из dict2.
    """


def m_5_4_2(dict1: dict, dict2: dict):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key].update(value)
        else:
            result[key] = value
    return result


# print(m_5_4_2(dict1, dict2))


# === Задача 3 ===
"""
    Дан словарь: Напишите программу, которая вернет
    список имен сотрудников из отдела "IT", чей возраст больше 25 лет.
    """


def m_5_4_3(data: dict, department="IT", age=25):
    result = [
        user["name"]
        for user in data.values()
        if user["department"] == department and user["age"] > age
    ]
    return result


# print(m_5_4_3(employees))


# === Задача 4 ===
"""
    Дан список словарей: Напишите программу, которая сгруппирует
    продукты по категориям и вернет новый вложенный словарь.
    """


def m_5_4_4(data: dict):
    result = {}
    for product in data:
        category = product["category"]
        info = {"name": product["name"], "price": product["price"]}
        result.setdefault(category, []).append(info)
    return result


# print(m_5_4_4(products))
