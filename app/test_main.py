import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 panny"),
        pytest.param(6, [1, 1, 0, 0], id="6 panny"),
        pytest.param(17, [2, 1, 1, 0], id="17 panny"),
        pytest.param(50, [0, 0, 0, 2], id="5 panny"),
    ]
)
def test_get_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result
