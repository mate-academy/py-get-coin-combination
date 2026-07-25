from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),      # 1 penny
        (6, [1, 1, 0, 0]),      # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),     # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),     # 2 quarters
    ]
)
def test_get_coin_combination_examples(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize("cents", [0, 1, 7, 13, 41, 99])
def test_total_value_equals_cents(cents: int) -> None:
    pennies, nickels, dimes, quarters = get_coin_combination(cents)
    total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25
    assert total == cents


@pytest.mark.parametrize(
    "cents, max_quarters",
    [
        (24, 0),
        (25, 1),
        (49, 1),
        (50, 2),
        (99, 3),
    ]
)
def test_uses_maximum_quarters(cents: int, max_quarters: int) -> None:
    coins = get_coin_combination(cents)
    assert coins[3] == max_quarters


def test_result_has_four_elements() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4
