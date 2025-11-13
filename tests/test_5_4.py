# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 5. Словари | Тип данных dict
# 5.4 Словари, как значения других словарей. Вложенные словари

import pytest
from src.module_5 import m_5_4_1, m_5_4_2, m_5_4_3, m_5_4_4

# для запуска pytest -k "test_5_4_" -q -x --tb=short


# === Тест для задачи 5.4.1 ===


@pytest.mark.parametrize(
    "data, field, expected",
    [
        # === sample sample ===
        (
            {
                "user1": {"name": "Alice", "age": 32, "score": 85},
                "user2": {"name": "Bob", "age": 28, "score": 92},
                "user3": {"name": "Charlie", "age": 35, "score": 88},
            },
            "score",
            "Bob",
        ),
        # === different field — maximum by age ===
        (
            {
                "user1": {"name": "Alice", "age": 32, "score": 85},
                "user2": {"name": "Bob", "age": 28, "score": 92},
                "user3": {"name": "Charlie", "age": 35, "score": 88},
            },
            "age",
            "Charlie",
        ),
        # === equal max values (first encountered stays) ===
        (
            {
                "u1": {"name": "Anna", "score": 90},
                "u2": {"name": "Bella", "score": 90},
                "u3": {"name": "Cara", "score": 85},
            },
            "score",
            "Anna",
        ),
        # === different field, like "salary" ===
        (
            {
                "dev1": {"name": "Tom", "salary": 3000},
                "dev2": {"name": "Jerry", "salary": 3500},
                "dev3": {"name": "Spike", "salary": 2500},
            },
            "salary",
            "Jerry",
        ),
        # === negative values ===
        (
            {
                "a": {"name": "Neo", "score": -10},
                "b": {"name": "Morpheus", "score": -5},
                "c": {"name": "Trinity", "score": -8},
            },
            "score",
            "Morpheus",
        ),
        # === float values ===
        (
            {
                "x": {"name": "Alice", "score": 9.7},
                "y": {"name": "Bob", "score": 9.9},
                "z": {"name": "Charlie", "score": 9.8},
            },
            "score",
            "Bob",
        ),
        # === single user dict ===
        (
            {"only": {"name": "Solo", "score": 100}},
            "score",
            "Solo",
        ),
    ],
    ids=[
        "base_sample",
        "max_by_age",
        "equal_max_values",
        "max_by_salary",
        "negative_values",
        "float_scores",
        "single_user",
    ],
)
def test_5_4_1(data, field, expected):
    assert m_5_4_1(data, field) == expected


# === Тест для задачи 5.4.2 ===


@pytest.mark.parametrize(
    "dict1, dict2, expected",
    [
        # === Sample test ===
        (
            {"A": {"x": 1, "y": 2}, "B": {"z": 3}},
            {"A": {"y": 5, "w": 8}, "C": {"k": 7}},
            {"A": {"x": 1, "y": 5, "w": 8}, "B": {"z": 3}, "C": {"k": 7}},
        ),
        # === Только непересекающиеся ключи ===
        (
            {"X": {"a": 1}, "Y": {"b": 2}},
            {"Z": {"c": 3}},
            {"X": {"a": 1}, "Y": {"b": 2}, "Z": {"c": 3}},
        ),
        # === Второй словарь полностью перекрывает первый ===
        (
            {"A": {"x": 10}},
            {"A": {"x": 20, "y": 30}},
            {"A": {"x": 20, "y": 30}},
        ),
        # === Смешанный случай ===
        (
            {"A": {"x": 1}, "B": {"y": 2}},
            {"A": {"z": 3}, "C": {"w": 4}},
            {"A": {"x": 1, "z": 3}, "B": {"y": 2}, "C": {"w": 4}},
        ),
        # === Пустой первый словарь ===
        (
            {},
            {"A": {"x": 1}},
            {"A": {"x": 1}},
        ),
        # === Пустой второй словарь ===
        (
            {"A": {"x": 1}},
            {},
            {"A": {"x": 1}},
        ),
    ],
    ids=[
        "sample_test",
        "non_overlapping_keys",
        "overwrite_inner_values",
        "mixed_case",
        "empty_first_dict",
        "empty_second_dict",
    ],
)
def test_5_4_2(dict1, dict2, expected):
    assert m_5_4_2(dict1, dict2) == expected


# === Тест для задачи 5.4.3 ===


@pytest.mark.parametrize(
    "data, department, age, expected",
    [
        # === sample test ===
        (
            {
                "emp1": {"name": "John", "age": 29, "department": "HR"},
                "emp2": {"name": "Anna", "age": 24, "department": "IT"},
                "emp3": {"name": "Mike", "age": 31, "department": "IT"},
                "emp4": {"name": "Sara", "age": 27, "department": "HR"},
            },
            "IT",
            25,
            ["Mike"],
        ),
        # === no employees matching ===
        (
            {
                "emp1": {"name": "John", "age": 22, "department": "IT"},
                "emp2": {"name": "Anna", "age": 24, "department": "IT"},
            },
            "IT",
            25,
            [],
        ),
        # === multiple matches in IT ===
        (
            {
                "emp1": {"name": "Eve", "age": 30, "department": "IT"},
                "emp2": {"name": "Mike", "age": 40, "department": "IT"},
                "emp3": {"name": "Sam", "age": 20, "department": "IT"},
            },
            "IT",
            25,
            ["Eve", "Mike"],
        ),
        # === test another department ===
        (
            {
                "emp1": {"name": "John", "age": 29, "department": "HR"},
                "emp2": {"name": "Anna", "age": 32, "department": "HR"},
                "emp3": {"name": "Mike", "age": 31, "department": "IT"},
            },
            "HR",
            25,
            ["John", "Anna"],
        ),
        # === age threshold — strictly greater ===
        (
            {
                "emp1": {"name": "Leo", "age": 25, "department": "IT"},
                "emp2": {"name": "Maya", "age": 26, "department": "IT"},
            },
            "IT",
            25,
            ["Maya"],
        ),
    ],
    ids=[
        "sample_case",
        "no_match",
        "multiple_in_it",
        "different_department",
        "age_threshold",
    ],
)
def test_5_4_3(data, department, age, expected):
    assert m_5_4_3(data, department, age) == expected


# === Тест для задачи 5.4.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # === sample test ===
        (
            [
                {"name": "Laptop", "category": "Electronics", "price": 1000},
                {"name": "Headphones", "category": "Electronics", "price": 200},
                {"name": "Coffee Maker", "category": "Home Appliances", "price": 150},
                {"name": "Blender", "category": "Home Appliances", "price": 120},
            ],
            {
                "Electronics": [
                    {"name": "Laptop", "price": 1000},
                    {"name": "Headphones", "price": 200},
                ],
                "Home Appliances": [
                    {"name": "Coffee Maker", "price": 150},
                    {"name": "Blender", "price": 120},
                ],
            },
        ),
        # === single category only ===
        (
            [
                {"name": "TV", "category": "Electronics", "price": 500},
                {"name": "Camera", "category": "Electronics", "price": 700},
            ],
            {
                "Electronics": [
                    {"name": "TV", "price": 500},
                    {"name": "Camera", "price": 700},
                ]
            },
        ),
        # === each product in a unique category ===
        (
            [
                {"name": "Sofa", "category": "Furniture", "price": 800},
                {"name": "Oven", "category": "Appliances", "price": 400},
                {"name": "Desk Lamp", "category": "Lighting", "price": 90},
            ],
            {
                "Furniture": [{"name": "Sofa", "price": 800}],
                "Appliances": [{"name": "Oven", "price": 400}],
                "Lighting": [{"name": "Desk Lamp", "price": 90}],
            },
        ),
        # === empty input ===
        ([], {}),
    ],
    ids=["sample_case", "single_category", "unique_categories", "empty_input"],
)
def test_5_4_4(data, expected):
    assert m_5_4_4(data) == expected
