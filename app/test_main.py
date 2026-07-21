from app.main import get_coin_combination


import pytest


@pytest.mark.parametrize(
    "num_of_coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (3, [3, 0, 0, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_simple_cases(num_of_coins: int, expected: list) -> None:
    actual = get_coin_combination(num_of_coins)
    assert actual == expected
    assert len(actual) == 4
    assert isinstance(actual, list)


@pytest.mark.parametrize(
    "old_number, new_number",
    [
        (4, 5),
        (9, 10),
        (24, 25),
        (29, 30),
        (34, 35),
        (49, 50),
    ]
)
def test_borders(old_number: int, new_number: int) -> None:
    old_number_of_coins = sum(get_coin_combination(old_number))
    new_number_of_coins = sum(get_coin_combination(new_number))
    assert new_number_of_coins < old_number_of_coins
