from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (15, [0, 1, 1, 0]),
        (35, [0, 0, 1, 1]),
        (1096, [1, 0, 2, 43])
    ],
    ids=str
)
def test_get_coin_combination(coins: int, expected: list) -> None:
    assert get_coin_combination(coins) == expected


def test_should_raise_type_error_if_coins_not_int() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("str")
