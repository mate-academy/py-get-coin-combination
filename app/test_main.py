import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (544, [4, 1, 1, 21])
    ],
    ids=[
        "zero cents in coins",
        "four cents in four pennies",
        "five cents in one nickels",
        "ten cents in one dimes",
        "twenty five cents in one quarters",
        "forty two cents in combine coins",
        "big value of cents in combine coins"
    ]
)
def test_coin_combinations(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
