import pytest
from app.main import get_coin_combination


def test_get_coin_combination_for_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_for_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_no_pennies() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
])
def test_parametrized_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
