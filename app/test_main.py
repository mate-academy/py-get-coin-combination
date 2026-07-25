import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test is cent zero"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test is cent 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test is cent 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test is cent 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test is cent 50"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="test is cent 41"
        ),
        pytest.param(
            30,
            [0, 1, 0, 1],
            id="30 cents"
        ),
        pytest.param(
            99,
            [4, 0, 2, 3],
            id="99 cents"
        ),
        pytest.param(
            28,
            [3, 0, 0, 1],
            id="28 cents"),
    ]
)
def test_coin_combination(cent: int, result: list[int]) -> None:
    coins = get_coin_combination(cent)
    assert coins == result
    values = [1, 5, 10, 25]
    assert sum(coin * value for coin, value in zip(coins, values)) == cent
