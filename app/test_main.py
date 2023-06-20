from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,num_of_pennies,num_of_nickels,num_of_dimes,num_of_quarters",
    [
        (0, 0, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (6, 1, 1, 0, 0),
        (17, 2, 1, 1, 0),
        (50, 0, 0, 0, 2),
        (67, 2, 1, 1, 2),
        (99, 4, 0, 2, 3),
        (100, 0, 0, 0, 4)
    ]
)
def test_correctly_coin_combinations(
        cents: int,
        num_of_pennies: int,
        num_of_nickels: int,
        num_of_dimes: int,
        num_of_quarters: int
) -> None:
    assert get_coin_combination(cents) == [
        num_of_pennies,
        num_of_nickels,
        num_of_dimes,
        num_of_quarters]
