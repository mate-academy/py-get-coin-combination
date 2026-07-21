import pytest

from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_returns_expected_combination(cents: int, expected: list[int]) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 25, 41, 50, 99, 100])
def test_returns_list_with_four_elements(cents: int) -> None:
    assert len(main.get_coin_combination(cents)) == 4


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 25, 41, 50, 99, 100])
def test_sum_of_coins_equals_cents(cents: int) -> None:
    pennies, nickels, dimes, quarters = main.get_coin_combination(cents)
    total = pennies + nickels * 5 + dimes * 10 + quarters * 25
    assert total == cents


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 25, 41, 50, 99, 100])
def test_all_counts_are_non_negative_integers(cents: int) -> None:
    coins = main.get_coin_combination(cents)
    assert all(isinstance(x, int) for x in coins)
    assert all(x >= 0 for x in coins)
