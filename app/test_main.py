import pytest as pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (52, [2, 0, 0, 2]),
    ],
    ids=[
        "0 cents should return 0 coins",
        "1 cent should return 1 penny",
        "6 cents should return 1 penny and 1 nickel",
        "17 cents should return 2 penny, 1 nickel and 1 dime",
        "52 cents should return 2 penny and 2 quarters",
    ]
)
def test_coin_combination(cents: int, expected_result: list[int]) -> None:
    assert (get_coin_combination(cents) == expected_result)
