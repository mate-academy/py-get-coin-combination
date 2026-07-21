import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="cents = 0, should return 0,0,0,0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="cents = 1, should return 1,0,0,0"
        ),
        pytest.param(
            7,
            [2, 1, 0, 0],
            id="cents = 7, should return 2,1,0,0"
        ),
        pytest.param(
            16,
            [1, 1, 1, 0],
            id="cents = 16, should return 1,1,1,0"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="cents = 41, should return 1,1,1,1"
        ),
        pytest.param(
            349,
            [4, 0, 2, 13],
            id="cents = 1, should return 4,0,2,13"
        )
    ]
)
def test_get_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
