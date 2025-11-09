# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 4.  Множества | Типы данных set и frozenset
# 4.3 Итерация по множествам и использование функций

import pytest
from src.module_4 import m_4_3_1, m_4_3_2, m_4_3_0

# для запуска pytest -k "test_4_3_" -q -x --tb=short


# === Тест для задачи 4.3.1 ===


@pytest.mark.parametrize(
    "nums, expected",
    [
        # sample test — matches the example from task
        ({10, 20, 30, 40, 50, 60, 70, 80, 90}, [60, 70, 80, 90]),
        # all numbers greater than 50 — full pass
        ({51, 52, 100, 999}, [51, 52, 100, 999]),
        # no numbers greater than 50 — empty result
        ({1, 2, 3, 4, 5, 6, 7}, []),
        # edge case — includes exactly 50, should exclude it
        ({45, 49, 50, 51, 52}, [51, 52]),
        # large range — checks performance and correctness
        (set(range(0, 101, 10)), [60, 70, 80, 90, 100]),
    ],
    ids=[
        "sample case",
        "all above 50",
        "none above 50",
        "includes 50 boundary",
        "large range 0-100 step 10",
    ],
)
def test_4_3_1(nums, expected):
    assert m_4_3_1(nums) == expected


# === Тест для задачи 4.3.2 ===


@pytest.mark.parametrize(
    "numbers, expected",
    [
        # sample case from task
        (
            {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20},
            (
                "[1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]\n"
                "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]"
            ),
        ),
        # only even numbers
        (
            {2, 4, 6, 8, 10, 12, 14, 15, 20},
            ("[2, 4, 6, 8, 12, 14]\n" "[2, 4, 6, 8, 10, 12, 14, 20]"),
        ),
        # contains only multiples of 5 — should become empty numbers list
        (
            {5, 10, 15, 20, 25},
            ("[]\n[10, 20]"),
        ),
        # no even numbers — even_numbers empty
        (
            {1, 3, 5, 7, 9, 11, 13, 15},
            ("[1, 3, 7, 9, 11, 13]\n[]"),
        ),
        # includes negative numbers and zero
        (
            {-10, -5, 0, 5, 10, 15, 20, 25, 30},
            ("[]\n[-10, 0, 10, 20, 30]"),
        ),
        # minimal input — empty set
        (set(), ("[]\n[]")),
    ],
    ids=[
        "sample case",
        "only evens with multiples of 5",
        "only multiples of 5",
        "no even numbers",
        "includes negatives and zero",
        "empty input",
    ],
)
def test_4_3_2(numbers, expected):
    assert m_4_3_2(numbers) == expected


# === Тест для дополнительных задач ===


def test_4_3_0():
    result = m_4_3_0()

    # === Task 1: unique numbers ===
    assert result[0] == {1, 2, 3, 4, 5}

    # === Task 2: unique words count ===
    assert result[1] == 4

    # === Task 3: intersection of two sets ===
    assert result[2] == {4, 5}

    # === Task 4: union of student names ===
    expected_students = {"Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Сергей"}
    assert result[3] == expected_students

    # === Task 5: divisible by 3 but not by 5 ===
    assert result[4] == {21, 42}
