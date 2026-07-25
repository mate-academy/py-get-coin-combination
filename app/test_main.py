import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (51, [1, 0, 0, 2]),
        (81, [1, 1, 0, 3]),
        (100, [0, 0, 0, 4]),
        (210, [0, 0, 1, 8])
    ],
    ids=[
        "Test check number of arguments that are returned",
        "Test return number of coins if cents equal to 1",
        "Test return number of coins if cents equal to 6",
        "Test return number of coins if cents equal to 17",
        "Test return number of coins if cents equal to 50",
        "Test return number of coins if cents equal to 51",
        "Test return number of coins if cents equal to 81",
        "Test return number of coins if cents equal to 100",
        "Test return number of coins if cents equal to 210"
    ]
)
def test_check_human_age_that_are_returned(
        cents: int,
        coins: list
) -> None:
    assert (get_coin_combination(cents) == coins), \
        f"Coins for {cents} cents should be equal to {coins}"


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        ("6", TypeError),
        (3.5, TypeError),
        (None, TypeError),
        ([5], TypeError),
        ({16}, TypeError),
        (-2, ValueError)
    ],
    ids=[
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect value of input data"
    ]
)
def test_raising_errors(
        cents: int,
        expected_error: TypeError | ValueError
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
