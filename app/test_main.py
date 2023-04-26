import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result_coin_combination",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="Check penny"),
        pytest.param(5, [0, 1, 0, 0],
                     id="Check nickel"),
        pytest.param(10, [0, 0, 1, 0],
                     id="Check dimes"),
        pytest.param(25, [0, 0, 0, 1],
                     id="Check quarter"),
        pytest.param(6, [1, 1, 0, 0],
                     id="Check pennies and nickels"),
        pytest.param(17, [2, 1, 1, 0],
                     id="Check pennies, nickels and dimes"),
        pytest.param(50, [0, 0, 0, 2],
                     id="Check dimes"),
        pytest.param(17, [2, 1, 1, 0],
                     id="Check pennies, nickels and dimes"),
        pytest.param(41, [1, 1, 1, 1],
                     id="Should return all coins")

    ]
)
def test_get_coin_combination(
        cents: int,
        result_coin_combination: list
) -> None:
    assert get_coin_combination(cents) == result_coin_combination
