import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(1, [1, 0, 0, 0], id="test 1 cent returns 1 penny"),
        pytest.param(
            6, [1, 1, 0, 0], id="test 6 cents returns 5 pennies, 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test 17 cents returns 2 pennies, 1 nickel, 1 dime",
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test 17 cents returns 2 pennies, 1 nickel, 1 dime",
        ),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> bool:
    assert get_coin_combination(cents) == expected
