from app.main import get_coin_combination
import pytest
from typing import List


# Тестування прикладів із завдання
@pytest.mark.parametrize(
    "cents, excepted",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_examples_from_task(
        cents: int,
        excepted: List[list]
) -> None:
    assert get_coin_combination(cents) == excepted


# Перевірка списка з 4 не відємних int
def test_return_contract() -> None:
    result = get_coin_combination(15)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
    assert all(x >= 0 for x in result)


# Перевірка меж nickel
@pytest.mark.parametrize(
    "cents, excepted",
    [
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
    ],
)
def test_boundaries_nickel(
        cents: int,
        excepted: List[list]
) -> None:
    assert get_coin_combination(cents) == excepted


# Перевірка меж для dime
@pytest.mark.parametrize(
    "cents, excepted",
    [
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
    ],
)
def test_boundaries_dime(
        cents: int,
        excepted: List[list]
) -> None:
    assert get_coin_combination(cents) == excepted


# Перевірка меж для quarter
@pytest.mark.parametrize(
    "cents, excepted",
    [
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
    ],
)
def test_boundaries_quarter(
        cents: int,
        excepted: List[list]
) -> None:
    assert get_coin_combination(cents) == excepted


# Тест на мінімальність
@pytest.mark.parametrize(
    "cents, excepted",
    [
        (20, [0, 0, 2, 0]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
    ],
)
def test_minimal_number_of_coins(
        cents: int,
        excepted: List[list]
) -> None:
    assert get_coin_combination(cents) == excepted


# Нуль і великі значення
def test_zero_amount() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount() -> None:
    cents = 999
    coins = get_coin_combination(cents)
    total = coins[0] + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
    assert total == cents


# Порядок елементів
def test_order_of_element() -> None:
    result = get_coin_combination(41)
    assert result[0] == 1
    assert result[1] == 1
    assert result[2] == 1
    assert result[3] == 1
