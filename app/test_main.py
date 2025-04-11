import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (52, [2, 0, 0, 2]),
        (-1, [4, 0, 2, -1]),
        (-6, [4, 1, 1, -1]),
        (-17, [3, 1, 0, -1]),
        (-52, [3, 0, 2, -3])
    ],
    ids=[
        "For 0 cent, result -> [0, 0, 0, 0]",
        "For 1 cent, result -> [1, 0, 0, 0]",
        "For 6 cent, result -> [1, 1, 0, 0]",
        "For 17 cent, result -> [2, 1, 1, 0]",
        "For 52 cent, result -> [2, 0, 0, 2]",
        "For -1 cent, result -> [4, 0, 2, -1]",
        "For -6 cent, result -> [4, 1, 1, -1]",
        "For -17 cent, result -> [3, 1, 0, -1]",
        "For -52 cent, result -> [3, 0, 2, -3]",
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    """
    Tests the get_coin_combination function, which returns the number
    of coins [1c, 5c, 10c, 25c] for a given amount of cents. Negative
    values are tested for correct handling.
    """
    assert get_coin_combination(cents) == expected
