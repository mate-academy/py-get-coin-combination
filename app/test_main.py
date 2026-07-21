import pytest
from app.main import get_coin_combination


def test_get_coin_combination_1_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_1_penny_1_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_2_pennies_1_nickel_1_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_2_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_0_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


if __name__ == "__main__":
    pytest.main()
