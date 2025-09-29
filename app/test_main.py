import pytest
from app.main import get_coin_combination


def test_zero_cents_returns_all_zeros() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_combination_with_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_exact_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_ninety_nine_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_one_dollar() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (7, [2, 1, 0, 0]),    # 2 pennies + 1 nickel
        (30, [0, 1, 0, 1]),   # 1 quarter + 1 nickel
        (41, [1, 1, 1, 1]),   # 1 penny + 1 nickel + 1 dime + 1 quarter
        (99, [4, 0, 2, 3]),   # 4 pennies + 2 dimes + 3 quarters
    ],
)
def test_parametrized_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_large_value_scaling() -> None:
    cents = 1234
    result = get_coin_combination(cents)
    total = (
        result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    )
    assert total == cents
