# Stepick.org — Python | Вторая ступень | Продвинутые концепции
# 4.  Множества | Типы данных set и frozenset
# 4.2 Операции с множествами

import pytest
from src.module_4 import m_4_2_1, m_4_2_2, m_4_2_3, m_4_2_4, m_4_2_5

# для запуска pytest -k "test_4_2_" -q -x --tb=short


# === Тест для задачи 4.2.1 ===


@pytest.mark.parametrize(
    "languages, element, expected",
    [
        ({"Python", "Java", "C++"}, "C++", ["Java", "Python"]),
        ({"Python", "JavaScript", "Go"}, "Go", ["JavaScript", "Python"]),
        ({"Ruby", "Swift", "Kotlin"}, "Ruby", ["Kotlin", "Swift"]),
        ({"HTML", "CSS", "JavaScript"}, "CSS", ["HTML", "JavaScript"]),
        ({"Rust", "TypeScript", "Elixir"}, "Rust", ["Elixir", "TypeScript"]),
    ],
    ids=[
        "basic-remove-C++",
        "remove-Go",
        "remove-first-in-alphabet",
        "remove-middle-element",
        "remove-non-latin-order",
    ],
)
def test_4_2_1(languages, element, expected):
    result = m_4_2_1(languages.copy(), element)
    assert result == expected


# === Тест для задачи 4.2.2 ===


@pytest.mark.parametrize(
    "set_a, set_b, expected",
    [
        ({10, 20, 30, 40}, {30, 40, 50}, "10, 20"),
        ({1, 2, 3, 4, 5}, {4, 5, 6}, "1, 2, 3"),
        ({100, 200, 300}, {400, 500}, "100, 200, 300"),
        ({7, 8, 9}, {7, 8, 9}, ""),
        ({5, 10, 15, 20}, set(), "5, 10, 15, 20"),
    ],
    ids=[
        "basic-difference",
        "partial-overlap",
        "no-overlap",
        "identical-sets",
        "empty-second-set",
    ],
)
def test_4_2_2(set_a, set_b, expected):
    result = m_4_2_2(set_a, set_b)
    assert result == expected


# === Тест для задачи 4.2.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("1 2\n3 4", ["1", "2", "3", "4"]),
        ("1 2 3\n3 4 5", ["1", "2", "4", "5"]),
        ("a b c\nd e f", ["a", "b", "c", "d", "e", "f"]),
        ("apple banana cherry\nbanana kiwi", ["apple", "cherry", "kiwi"]),
        ("1 1 1 2 3\n2 3 4", ["1", "4"]),
        ("10 20 30\n10 20 30", []),
        ("\n\n", []),
        (" \n1", ["1"]),
    ],
    ids=[
        "base_case_no_overlap",
        "overlap_single_value",
        "letters_disjoint",
        "words_with_common",
        "duplicates_in_input",
        "identical_lists",
        "empty_input_lines",
        "one_empty_one_filled",
    ],
)
def test_4_2_3(data, expected):
    assert m_4_2_3(data) == expected


# === Тест для задачи 4.2.4 ===


@pytest.mark.parametrize(
    "anna, boris, expected",
    [
        # partial overlap
        (
            {"Иван", "Мария", "Петр", "Елена"},
            {"Петр", "Елена", "Сергей", "Анна"},
            "['Елена', 'Петр']\n"
            "['Анна', 'Елена', 'Иван', 'Мария', 'Петр', 'Сергей']\n"
            "['Иван', 'Мария']",
        ),
        # no common friends
        (
            {"Алиса", "Боб", "Чарли"},
            {"Дэвид", "Ева"},
            "[]\n"
            "['Алиса', 'Боб', 'Дэвид', 'Ева', 'Чарли']\n"
            "['Алиса', 'Боб', 'Чарли']",
        ),
        # identical sets
        (
            {"Анна", "Борис"},
            {"Анна", "Борис"},
            "['Анна', 'Борис']\n" "['Анна', 'Борис']\n" "[]",
        ),
        # single element each
        (
            {"Анна"},
            {"Борис"},
            "[]\n" "['Анна', 'Борис']\n" "['Анна']",
        ),
        # anna has no friends
        (
            set(),
            {"Анна", "Борис"},
            "[]\n" "['Анна', 'Борис']\n" "[]",
        ),
        # boris has no friends
        (
            {"Анна", "Борис"},
            set(),
            "[]\n" "['Анна', 'Борис']\n" "['Анна', 'Борис']",
        ),
    ],
    ids=[
        "partial overlap",
        "no common friends",
        "identical sets",
        "single element each",
        "anna has no friends",
        "boris has no friends",
    ],
)
def test_4_2_4(anna, boris, expected):
    assert m_4_2_4(anna, boris) == expected


# === Тест для задачи 4.2.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # basic case — from the sample
        (
            "Python прост в изучении и python является отличным "
            "отличным инструментом для решения задач",
            "11\n['python', 'в', 'для', 'задач', 'и', 'изучении', "
            "'инструментом', 'отличным', 'прост', 'решения', 'является']",
        ),
        # same word repeated many times
        (
            "hello hello hello hello",
            "1\n['hello']",
        ),
        # mixed case — should normalize to lowercase
        (
            "One two TWO Three three THREE",
            "3\n['one', 'three', 'two']",
        ),
        # empty input
        (
            "",
            "0\n[]",
        ),
        # single word
        (
            "Alone",
            "1\n['alone']",
        ),
    ],
    ids=[
        "sample text",
        "repeated single word",
        "mixed case normalization",
        "empty input",
        "single word",
    ],
)
def test_4_2_5(data, expected):
    assert m_4_2_5(data) == expected
