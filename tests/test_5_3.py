# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 5. Словари | Тип данных dict
# 5.3 Основные методы словарей | keys() values() items() get()

import pytest
from src.module_5 import m_5_3_1, m_5_3_2, m_5_3_3, m_5_3_4

# для запуска pytest -k "test_5_3_" -q -x --tb=short


# === Тест для задачи 5.3.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # === base case ===
        (
            {
                "apple": 10,
                "banana": 5,
                "orange": 7,
                "grapes": 3,
                "melon": 2,
            },
            [10, 5, 7, 3, 2],
        ),
        # === simple numeric keys ===
        (
            {1: 100, 2: 200, 3: 300},
            [100, 200, 300],
        ),
        # === mixed key types ===
        (
            {"x": 1, 2: "b", (3, 4): True},
            [1, "b", True],
        ),
        # === single element ===
        (
            {"only": 42},
            [42],
        ),
        # === empty dictionary ===
        (
            {},
            [],
        ),
    ],
    ids=["base_case", "numeric_keys", "mixed_keys", "single_item", "empty_dict"],
)
def test_5_3_1(data, expected):
    result = list(m_5_3_1(data))  # dict_values → list для сравнения
    assert result == expected


# === Тест для задачи 5.3.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # === base case ===
        (
            {
                "apple": 10,
                "banana": 5,
                "orange": 7,
                "grapes": 3,
                "melon": 2,
            },
            ["apple", "banana", "orange", "grapes", "melon"],
        ),
        # === numeric keys ===
        (
            {1: "a", 2: "b", 3: "c"},
            [1, 2, 3],
        ),
        # === mixed key types ===
        (
            {"x": 10, (1, 2): 20, 3: 30},
            ["x", (1, 2), 3],
        ),
        # === single key ===
        (
            {"only": 1},
            ["only"],
        ),
        # === empty dict ===
        (
            {},
            [],
        ),
    ],
    ids=["base_case", "numeric_keys", "mixed_keys", "single_key", "empty_dict"],
)
def test_5_3_2(data, expected):
    result = list(m_5_3_2(data))
    assert result == expected


# === Тест для задачи 5.3.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # === base case ===
        (
            {
                "apple": 10,
                "banana": 5,
                "orange": 7,
                "grapes": 3,
                "melon": 2,
            },
            "apple: 10\nbanana: 5\norange: 7\ngrapes: 3\nmelon: 2",
        ),
        # === numeric keys ===
        (
            {1: "a", 2: "b"},
            "1: a\n2: b",
        ),
        # === mixed types ===
        (
            {"x": 10, 42: "answer"},
            "x: 10\n42: answer",
        ),
        # === single pair ===
        (
            {"only": 1},
            "only: 1",
        ),
        # === empty dict ===
        (
            {},
            "",
        ),
    ],
    ids=[
        "base_case",
        "numeric_keys",
        "mixed_types",
        "single_pair",
        "empty_dict",
    ],
)
def test_5_3_3(data, expected):
    result = m_5_3_3(data)
    assert result == expected


# === Тест для задачи 5.3.4 ===


@pytest.mark.parametrize(
    "data, queries, expected",
    [
        # === base case ===
        (
            {
                "apple": 10,
                "banana": 5,
                "orange": 7,
                "grapes": 3,
                "melon": 2,
            },
            ("banana", "pear"),
            "5\nNot found",
        ),
        # === pear key present ===
        (
            {"banana": 42, "pear": 0},
            ("banana", "pear"),
            "42\n0",
        ),
        # === neither banana nor pear exist ===
        (
            {"apple": 1, "melon": 2},
            ("banana", "pear"),
            "Not found\nNot found",
        ),
        # === only banana present ===
        (
            {"banana": 100, "melon": 5},
            ("banana", "pear"),
            "100\nNot found",
        ),
        # === custom queries, both exist ===
        (
            {"cat": 3, "dog": 5, "fish": 2},
            ("dog", "fish"),
            "5\n2",
        ),
        # === custom queries, mixed presence ===
        (
            {"x": 1, "y": 2, "z": 3},
            ("a", "z"),
            "Not found\n3",
        ),
        # === single query tuple ===
        (
            {"python": 42},
            ("python",),
            "42",
        ),
        # === empty dict ===
        (
            {},
            ("banana", "pear"),
            "Not found\nNot found",
        ),
        # === completely custom search set ===
        (
            {"a": 1, "b": 2, "c": 3},
            ("b", "x", "a"),
            "2\nNot found\n1",
        ),
    ],
    ids=[
        "base_case",
        "pear_key_present",
        "no_banana_no_pear",
        "banana_only",
        "custom_queries_exist",
        "mixed_queries",
        "single_query",
        "empty_dict",
        "multiple_custom_queries",
    ],
)
def test_5_3_4(data, queries, expected):
    result = m_5_3_4(data, queries)
    assert result == expected
