import pytest
from app.main import get_coin_combination


def test_zero_cents() -> None:
    # ANN201 fix: Added -> None
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_single_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_single_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_single_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_multiple_quarters() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


@pytest.mark.parametrize("cents, expected", [
    (6, [1, 1, 0, 0]),
    (11, [1, 0, 1, 0]),
    (24, [4, 0, 2, 0]),
    (99, [4, 0, 2, 3]),
])
def test_various_amounts(cents: int, expected: list) -> None:
    # ANN001 fix: Added : int and : list
    # ANN201 fix: Added -> None
    assert get_coin_combination(cents) == expected
