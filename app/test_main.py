import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        # check if cents less than 5
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="less then 5 cents"
        ),
        pytest.param(
            7,
            [2, 1, 0, 0],
            id="more than 5 less then 10 cents"
        ),
        pytest.param(
            18,
            [3, 1, 1, 0],
            id="more than 10 less then 25 cents"
        ),
        pytest.param(
            43,
            [3, 1, 1, 1],
            id="more than 25 cents"
        ),
        pytest.param(
            75,
            [0, 0, 0, 3],
            id="cents amount multiple of 25"
        ),
        pytest.param(
            45,
            [0, 0, 2, 1],
            id="cents amount multiple of 10 and  25"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="zero cents"
        ),
    ]
)
def test_correct_coins_count(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents) == coins
