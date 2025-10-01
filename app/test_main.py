from app.main import get_coin_combination
import pytest


def test_return_with_negative_number() -> None:
    assert get_coin_combination(-5) == [0, 0, 2, -1]


@pytest.mark.parametrize(
    ["coins", "result"],
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_right_results_core_logic(coins: int, result: list[int]) -> None:
    assert get_coin_combination(coins) == result


@pytest.mark.parametrize(
    ["coins"],
    [
        (1.0,),
        (6.5,),
        (17.2,),
        (50.1,),
    ]
)
def test_return_if_coins_is_float(coins: int) -> None:
    assert all(isinstance(x, float) for x in get_coin_combination(coins))
