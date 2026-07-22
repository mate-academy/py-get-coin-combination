import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        # zero amount
        (0, [0, 0, 0, 0]),

        # pennies only (1-4 cents)
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (4, [4, 0, 0, 0]),

        # exact nickel / nickel boundary
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),

        # exact dime / dime boundary
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (19, [4, 1, 1, 0]),

        # two dimes
        (20, [0, 0, 2, 0]),
        (24, [4, 0, 2, 0]),

        # exact quarter / quarter boundary
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (29, [4, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (34, [4, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (44, [4, 1, 1, 1]),
        (45, [0, 0, 2, 1]),
        (49, [4, 0, 2, 1]),

        # two quarters and beyond
        (50, [0, 0, 0, 2]),
        (74, [4, 0, 2, 2]),
        (75, [0, 0, 0, 3]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),

        # a larger, arbitrary amount
        (287, [2, 0, 1, 11]),
    ],
)
def test_get_coin_combination_values(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_returns_a_list() -> None:
    assert isinstance(get_coin_combination(17), list)


def test_returns_four_elements() -> None:
    assert len(get_coin_combination(17)) == 4


def test_result_reconstructs_original_amount() -> None:
    coin_values = (1, 5, 10, 25)
    for cents in range(0, 200):
        pennies, nickels, dimes, quarters = get_coin_combination(cents)
        total = sum(
            count * value
            for count, value in zip(
                (pennies, nickels, dimes, quarters), coin_values
            )
        )
        assert total == cents


def test_result_uses_minimum_number_of_coins() -> None:
    # Pennies should never reach 5 (would be replaced by a nickel),
    # nickels should never reach 2 (would be replaced by a dime),
    # dimes should never reach 3 in a way that isn't better as quarters.
    for cents in range(0, 200):
        pennies, nickels, dimes, quarters = get_coin_combination(cents)
        assert pennies < 5
        assert nickels < 2
        assert dimes < 3
