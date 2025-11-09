# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 4.  Множества | Типы данных set и frozenset
# 4.4 Замороженные множества | Тип данных frozenset

import pytest
from src.module_4 import m_4_4_1, m_4_4_2, m_4_4_3

# для запуска pytest -k "test_4_4_" -q -x --tb=short


# === Tests for 4.4.1 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ([1, 2, 2, 3, 3, 3], frozenset({1, 2, 3})),  # basic case with duplicates
        (["apple", "banana", "apple"], frozenset({"apple", "banana"})),  # strings
        ([], frozenset()),  # empty list
        ([42], frozenset({42})),  # single element
    ],
    ids=[
        "integers_with_duplicates",
        "strings_with_duplicates",
        "empty_list",
        "single_element",
    ],
)
def test_4_4_1(data, expected):
    result = m_4_4_1(data)
    assert result == expected
    assert isinstance(result, frozenset)


# === Tests for 4.4.2: Basic frozenset operations ===


def test_4_4_2():
    nums, contains_three, length = m_4_4_2()
    assert nums == frozenset({1, 2, 3, 4, 5})
    assert contains_three is True
    assert length == 5


# === Tests for 4.4.3: frozenset relations and operations ===
@pytest.mark.parametrize(
    "fset1, fset2, expected_union, expected_intersection, expected_difference, subset_check",
    [
        (
            frozenset({1, 2, 3, 4, 5}),
            frozenset({4, 5, 6, 7}),
            frozenset({1, 2, 3, 4, 5, 6, 7}),  # union
            frozenset({4, 5}),  # intersection
            frozenset({1, 2, 3}),  # difference
            True,  # is superset of {3, 4}
        ),
        (
            frozenset({10, 20, 30}),
            frozenset({30, 40}),
            frozenset({10, 20, 30, 40}),
            frozenset({30}),
            frozenset({10, 20}),
            False,
        ),
    ],
    ids=["default_sets", "custom_sets"],
)
def test_4_4_3(
    fset1,
    fset2,
    expected_union,
    expected_intersection,
    expected_difference,
    subset_check,
):
    union, intersection, difference, superset_func = m_4_4_3(fset1, fset2)
    assert union == expected_union
    assert intersection == expected_intersection
    assert difference == expected_difference
    assert superset_func({3, 4}) is subset_check
