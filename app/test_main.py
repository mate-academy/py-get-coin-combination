from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "coins,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="0 coins"),
        pytest.param(1, [1, 0, 0, 0], id="1 coin"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents"),
        pytest.param(41, [1, 1, 1, 1], id="0 coins"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents"),
    ])
def test_get_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result


@pytest.mark.parametrize(
    "invalid_coins_type",
    [
        pytest.param(15.5, id="float value"),
        pytest.param("15", id="string value"),
        pytest.param([15], id="list value"),
    ]
)
def test_get_invalid_coin_type(invalid_coins_type: float | str | list) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(invalid_coins_type)


@pytest.mark.parametrize(
    "negative_coins_value",
    [
        pytest.param(-1, id="negative value"),
    ]
)
def test_get_negative_coins_value(negative_coins_value: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(negative_coins_value)
