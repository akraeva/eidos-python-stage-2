# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 4.  Множества | Типы данных set и frozenset
# 4.1 Введение в множества | Тип данных set

import pytest
from src.module_4 import m_4_1_1

# для запуска pytest -k "test_4_1_" -q -x --tb=short


# === Тест для задачи 4.1.1 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        pytest.param(
            "1 2 1 3 1 2 4 5 6 1 2 1 7",
            [1, 2, 3, 4, 5, 6, 7],
            id="basic-mixed-repetitions",
        ),
        pytest.param(
            "10 9 8 7 6 5 4 3 2 1",
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            id="descending-order-input",
        ),
        pytest.param("5 5 5 5 5", [5], id="all-elements-identical"),
        pytest.param("   3   1   2   3   1   ", [1, 2, 3], id="extra-spaces-around"),
        pytest.param("0 0 0 1 2 0 3 0 4 0", [0, 1, 2, 3, 4], id="includes-zero"),
        pytest.param(
            "-5 -10 0 5 10 -5 0", [-10, -5, 0, 5, 10], id="negative-and-positive"
        ),
        pytest.param("42", [42], id="single-element"),
    ],
)
def test_4_1_1(data, expected):
    assert m_4_1_1(data) == expected
