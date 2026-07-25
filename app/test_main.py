from app.main import get_coin_combination
import pytest


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_only_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_combination_of_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
    assert get_coin_combination(123) == [3, 0, 2, 4]


if __name__ == "__main__":
    pytest.main()
