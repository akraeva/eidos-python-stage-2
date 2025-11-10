# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 5. Словари | Тип данных dict
# 5.1 Введение в словари | dict()

import pytest
from src.module_5 import m_5_1_1, m_5_1_2

# для запуска pytest -k "test_5_1_" -q -x --tb=short


# === Тест для задачи 5.1.1 ===


@pytest.mark.parametrize(
    "pupil, expected",
    [
        # Author example: base case
        (
            {"name": "John", "age": 25, "city": "London", "is_student": True},
            {"name": "John", "age": 28, "city": "London", "is_student": False},
        ),
        # Custom case 1: older student
        (
            {"name": "Bob", "age": 40, "city": "Berlin", "is_student": True},
            {"name": "Bob", "age": 43, "city": "Berlin", "is_student": False},
        ),
        # Custom case 2: already not a student (should remain False)
        (
            {"name": "Ann", "age": 22, "city": "Rome", "is_student": False},
            {"name": "Ann", "age": 25, "city": "Rome", "is_student": False},
        ),
    ],
    ids=["base_case", "older_student", "already_not_student"],
)
def test_5_1_1(pupil, expected):
    result = m_5_1_1(pupil.copy())
    assert result == expected
    assert result is not pupil


# === Tests for 5.1.2: Add new city key to dict ===
@pytest.mark.parametrize(
    "student, expected",
    [
        # Author example: base case
        (
            {"name": "John", "age": 28, "city": "London", "is_student": False},
            {"name": "Alice", "age": 21, "city": "Paris"},
        ),
        # Custom case 1: input completely ignored, still returns Alice
        (
            {"name": "Random", "age": 99},
            {"name": "Alice", "age": 21, "city": "Paris"},
        ),
        # Custom case 2: check idempotency (repeated call gives same result)
        (
            {"name": "Alice", "age": 21},
            {"name": "Alice", "age": 21, "city": "Paris"},
        ),
    ],
    ids=["base_case", "ignored_input", "idempotent_call"],
)
def test_5_1_2(student, expected):
    result = m_5_1_2(student)
    assert result == expected
    assert isinstance(result, dict)
    assert "city" in result
    assert result["city"] == "Paris"
