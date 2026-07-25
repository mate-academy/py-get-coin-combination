import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("number_of_coins, expected", [
    pytest.param(
        1, [1, 0, 0, 0],
        id="should return one penny"
    ),
    pytest.param(
        6, [1, 1, 0, 0],
        id="should return one penny and one nickel"
    ),
    pytest.param(
        17, [2, 1, 1, 0],
        id="should return two pennies, one nickel and one dime"
    ),
    pytest.param(
        50, [0, 0, 0, 2],
        id="should return two quarters"
    ),
])
def test_coins(number_of_coins: int, expected: list) -> None:
    assert get_coin_combination(number_of_coins) == expected
