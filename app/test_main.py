import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 cent equal to 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="6 cents equal to 1 penny + 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="17 cents equal to 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="50 cents equal to 2 quarters"
        ),

    ]
)
def test_get_coin_combination(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result
