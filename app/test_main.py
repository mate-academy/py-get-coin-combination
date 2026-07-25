import pytest
from app.main import get_coin_combination


def test_get_coin_combination_with_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], "1 penny"


def test_get_coin_combination_with_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0], "1 penny + 1 nickel"


def test_get_coin_combination_with_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0], (
        "2 pennies + 1 nickel + 1 dime"
    )


def test_get_coin_combination_with_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2], "2 quarters"


def test_get_coin_combination_with_0_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0], "0 cents"


def test_get_coin_combination_with_large_amount_2() -> None:
    assert get_coin_combination(123) == [3, 0, 2, 4], (
        "3 pennies + 2 dimes + 4 quarters"
    )


def test_get_coin_combination_with_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3], (
        "4 pennies + 2 dimes + 3 quarters"
    )


if __name__ == "__main__":
    pytest.main()
