import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="zero cents"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="just one penny"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="just one nickel"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="just one dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="just one quarter"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="max before nickel"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="max before dime"
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id="max before quarter"
        ),
        pytest.param(
            104,
            [4, 0, 0, 4],
            id="random mix"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="every coin"
        ),
        pytest.param(
            33343,
            [3, 1, 1, 1333],
            id="large number"
        ),
    ]
)
def test_combine_coins_correctly(
        cents: int,
        coins: list[int]
) -> None:
    assert get_coin_combination(cents) == coins
