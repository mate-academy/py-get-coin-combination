import pytest

import app.main as main_module


@pytest.mark.parametrize("cents,expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (11, [1, 0, 1, 0]),
    (15, [0, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (26, [1, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main_module.get_coin_combination(cents) == expected


def test_returns_list() -> None:
    assert isinstance(main_module.get_coin_combination(0), list)


def test_returns_four_elements() -> None:
    assert len(main_module.get_coin_combination(0)) == 4


def test_uses_minimum_number_of_coins() -> None:
    result = main_module.get_coin_combination(30)
    assert sum(result) == 2


def test_coins_sum_equals_cents() -> None:
    cents = 87
    result = main_module.get_coin_combination(cents)
    total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total == cents


def test_zero_cents_returns_all_zeros() -> None:
    assert main_module.get_coin_combination(0) == [0, 0, 0, 0]


def test_pennies_are_last_resort() -> None:
    result = main_module.get_coin_combination(25)
    assert result[0] == 0


def test_large_amount() -> None:
    result = main_module.get_coin_combination(1000)
    assert result == [0, 0, 0, 40]
