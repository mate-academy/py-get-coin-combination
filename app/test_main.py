import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (68, [3, 1, 1, 2]),
    ],
    ids=[
        "should return all zeros when sum is 0",
        "should return one coin when sum exactly matches nominal",
        "should return correct mixture of small coins",
        "should return at least one of every coin type",
        "should return correct combination for a large sum",
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
