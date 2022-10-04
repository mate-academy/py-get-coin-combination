import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "get_cents,expected_result",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return minimal of the smallest possible number of coins"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return minimal numbers of coins what equal same amount"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should return [2, 1, 1, 0], 2 pennies + 1 nickel + 1 dime "
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should return [0, 0, 0, 2], 2 quarters"
        )
    ]
)
def test_get_coin_combination(get_cents, expected_result):
    assert get_coin_combination(get_cents) == expected_result
