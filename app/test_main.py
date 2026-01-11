import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(25, [0, 0, 0, 1], id="number of quarters"),
        pytest.param(10, [0, 0, 1, 0], id="number of dimes"),
        pytest.param(14, [4, 0, 1, 0], id="number of pennies and dimes"),
        pytest.param(5, [0, 1, 0, 0], id="number of nickels"),
        pytest.param(9, [4, 1, 0, 0], id="number of pennies and nickels"),
        pytest.param(4, [4, 0, 0, 0], id="number of pennies")
    ]
)
def test_number_of_coins(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
