from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "given_coin,expect",
    [
        (
            1,
            [1, 0, 0, 0]
        ),
        (
            6,
            [1, 1, 0, 0]
        ),
        (
            17,
            [2, 1, 1, 0]
        ),
        (
            50,
            [0, 0, 0, 2]
        )
    ]
)
def test(given_coin, expect):
    assert get_coin_combination(given_coin) == expect
