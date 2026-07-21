import pytest

from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_large_amount() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(123) == [3, 0, 2, 4]


@pytest.mark.parametrize(
    "cents,expected", [
        (7, [2, 1, 0, 0]),
        (32, [2, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
    ]
)
def test_parametrized_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
