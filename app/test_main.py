from app.main import get_coin_combination

import pytest

@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 cent",
        "6 cents",
        "17 cents",
        "50 cents"
    ]
)
def test_should_return_correct_combination_of_coins(
    cents: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected, \
        f"Combination of coins should be {expected} for {cents} cents"