import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero cents",
        "one penny",
        "only pennies",
        "one nickel",
        "penny and nickel",
        "one dime",
        "nickel and dime",
        "pennies, nickel and dime",
        "two dimes, not nickels",
        "one quarter",
        "one of each coin",
        "two quarters",
        "all coin types, max change",
    ],
)
def test_should_return_smallest_coin_combination(
    cents: int,
    expected_coins: list[int],
) -> None:
    assert main.get_coin_combination(cents) == expected_coins


def test_should_return_list() -> None:
    assert isinstance(main.get_coin_combination(17), list)
