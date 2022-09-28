from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,coin",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny if cents == 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should added nickels if coins > 5"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should added dime if coins > 10"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should added quarters if coins >= 25"
        )
    ]
)
def test_get_coin_combination_correctly(cents: int, coin: list):
    assert get_coin_combination(cents) == coin
