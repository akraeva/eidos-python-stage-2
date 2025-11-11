# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 5. Словари | Тип данных dict
# 5.2 Методы изменения словарей | del() pop() popitem() clear()

import pytest
from src.module_5 import m_5_2_1

# для запуска pytest -k "test_5_2_" -q -x --tb=short


# === Тест для задачи 5.2.1 ===


@pytest.mark.parametrize(
    "inventory, expected",
    [
        # === Author example ===
        (
            {
                "apple": 10,
                "banana": 5,
                "orange": 7,
                "grapes": 3,
                "melon": 2,
            },
            "\n".join(
                [
                    "После добавления элементов: {'apple': 15, 'banana': 7, 'orange': 7, 'grapes': 3, 'melon': 2}",
                    "После удаления элементов: {'apple': 15, 'banana': 7, 'grapes': 2, 'melon': 2}",
                    "После обновления значений: {'apple': 15, 'banana': 7, 'grapes': 2, 'melon': 2, 'watermelon': 4}",
                    "Количество арбузов (melon): 2",
                    "После проверки наличия элемента: {'apple': 15, 'banana': 7, 'grapes': 2, 'melon': 2, 'watermelon': 4}",
                    "Удаленный элемент: ('watermelon', 4)",
                    "После использования popitem(): {'apple': 15, 'banana': 7, 'grapes': 2, 'melon': 2}",
                    "После очистки инвентаря: {}",
                ]
            ),
        ),
        # === Custom case 1: без апельсинов в начале ===
        (
            {
                "apple": 3,
                "banana": 10,
                "grapes": 5,
                "melon": 1,
            },
            "\n".join(
                [
                    "После добавления элементов: {'apple': 8, 'banana': 12, 'grapes': 5, 'melon': 1}",
                    "После удаления элементов: {'apple': 8, 'banana': 12, 'grapes': 4, 'melon': 1}",
                    "После обновления значений: {'apple': 8, 'banana': 12, 'grapes': 4, 'melon': 1, 'watermelon': 4}",
                    "Количество арбузов (melon): 1",
                    "После проверки наличия элемента: {'apple': 8, 'banana': 12, 'grapes': 4, 'melon': 1, 'watermelon': 4}",
                    "Удаленный элемент: ('watermelon', 4)",
                    "После использования popitem(): {'apple': 8, 'banana': 12, 'grapes': 4, 'melon': 1}",
                    "После очистки инвентаря: {}",
                ]
            ),
        ),
        # === Custom case 2: без дыни (melon) изначально ===
        (
            {
                "apple": 5,
                "banana": 2,
                "orange": 3,
                "grapes": 2,
            },
            "\n".join(
                [
                    "После добавления элементов: {'apple': 10, 'banana': 4, 'orange': 3, 'grapes': 2}",
                    "После удаления элементов: {'apple': 10, 'banana': 4, 'grapes': 1}",
                    "После обновления значений: {'apple': 10, 'banana': 4, 'grapes': 1, 'watermelon': 4}",
                    "Количество арбузов (melon): 0",
                    "После проверки наличия элемента: {'apple': 10, 'banana': 4, 'grapes': 1, 'watermelon': 4}",
                    "Удаленный элемент: ('watermelon', 4)",
                    "После использования popitem(): {'apple': 10, 'banana': 4, 'grapes': 1}",
                    "После очистки инвентаря: {}",
                ]
            ),
        ),
    ],
    ids=["base_case", "no_orange", "no_melon"],
)
def test_5_2_1(inventory, expected):
    result = m_5_2_1(inventory.copy())
    assert result == expected
