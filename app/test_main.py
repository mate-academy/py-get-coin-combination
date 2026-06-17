import pytest

from app.main import get_coin_combination


# write your tests here
@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]), #1 penny
        (6, [1, 1, 0, 0]), #1 penny + 1 nickel
        (17, [2, 1, 1, 0]), #2 penny + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]) #2 quarters
    ]
)
def test_get_coin_combination(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected