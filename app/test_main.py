import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value, cents",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="Value == 1 must return 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Value == 6 must return 1 penny + 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Value == 17 must return 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Value == 50 must return 2 quarters"
        ),
    ]
)
def test_get_coin_combination(value: int, cents: list) -> None:
    assert get_coin_combination(value) == cents
