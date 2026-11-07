import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_should_return_smallest_number_of_coins(
    cents: int,
    expected: list
) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [0, 1, 5, 10, 25, 17, 49, 99, 100, 123],
)
def test_coins_should_sum_up_to_given_amount(cents: int) -> None:
    pennies, nickels, dimes, quarters = main.get_coin_combination(cents)
    assert pennies + nickels * 5 + dimes * 10 + quarters * 25 == cents


@pytest.mark.parametrize("cents", [0, 3, 17, 49, 99, 123])
def test_should_return_list_of_four_elements(cents: int) -> None:
    assert len(main.get_coin_combination(cents)) == 4


@pytest.mark.parametrize("cents", [4, 9, 14, 24, 49, 99])
def test_should_use_at_most_four_pennies(cents: int) -> None:
    assert main.get_coin_combination(cents)[0] <= 4
