import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (19, [4, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (29, [4, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (39, [4, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (123, [3, 0, 2, 4]),
        (999, [4, 0, 2, 39]),
        (1000, [0, 0, 0, 40]),
    ]
)
def test_coin_combination_expected_results(
    cents: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


def test_coin_combination_returns_list() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)


def test_coin_combination_has_four_elements() -> None:
    result = get_coin_combination(63)
    assert len(result) == 4


def test_coin_combination_contains_integers() -> None:
    result = get_coin_combination(78)
    assert all(isinstance(coin, int) for coin in result)


def test_coin_combination_has_no_negative_counts() -> None:
    result = get_coin_combination(142)
    assert all(coin >= 0 for coin in result)


def test_coin_combination_total_value() -> None:
    result = get_coin_combination(187)
    pennies, nickels, dimes, quarters = result

    total = (
        pennies
        + nickels * 5
        + dimes * 10
        + quarters * 25
    )

    assert total == 187


def test_coin_combination_minimum_number_of_coins() -> None:
    result = get_coin_combination(88)
    assert sum(result) == 7
