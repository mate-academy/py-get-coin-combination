import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_numbers_of_coins",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="for 1 cent result should be 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="for 6 cents result should be 1 penny and 1 nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="for 17 cents result should be "
                        "2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2],
                     id="for 6 cents result should be 2 quarters"),
        pytest.param(42, [2, 1, 1, 1],
                     id="for 41 cents result should be 2 pennies +"
                        " 1 nickel + 1 dime + 1 quarter")
    ]
)
def test_get_human_age(cents: int,
                       expected_numbers_of_coins: list) -> None:
    assert expected_numbers_of_coins == get_coin_combination(cents)
