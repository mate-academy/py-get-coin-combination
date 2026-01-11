import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents", [2, 5, 24, 124, 23, 65, 22])
def test_preserves_total_value(
    cents: int
) -> None:
    pennies, nickels, dimes, quarters = get_coin_combination(cents)
    total_coins_value = pennies + 5 * nickels + 10 * dimes + 25 * quarters
    assert cents == total_coins_value, (
        "No money should be lost or gained"
    )


def test_returns_list_of_zeroes_when_cents_are_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0], (
        "Must return [0, 0, 0, 0] when cents == 0"
    )


@pytest.mark.parametrize("cents", [1, 2, 3, 4])
def test_returns_only_pennies_for_less_than_5_cents(cents: int) -> None:
    coins = get_coin_combination(cents)
    assert coins[0] == cents and not any(coins[1:]), (
        "Must return pennies only when cents < 5"
    )


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (20, [0, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (125, [0, 0, 0, 5])
    ]
)
def test_returns_coins_with_highest_value_when_cents_are_divisible_by_it(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected, (
        "Must return coins of the highest value when cents are divisible by it"
        "e.g. 125 cents must become 5 quarters"
    )


@pytest.mark.parametrize(
    "cents,expected",
    [
        (6, [1, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (26, [1, 0, 0, 1]),
        (15, [0, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (16, [1, 1, 1, 0]),
        (31, [1, 1, 0, 1]),
        (36, [1, 0, 1, 1]),
    ]
)
def test_returns_mixed_coins(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected, (
        "Must be able to correctly give mixed coins"
    )
