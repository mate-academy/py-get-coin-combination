from app.main import get_coin_combination
import pytest


def test_correct_returned_instances() -> None:
    coins = get_coin_combination(10)
    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all([isinstance(coin, int) for coin in coins])


@pytest.mark.parametrize(
    "coin, expected",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (160, [0, 0, 1, 6]),
        (256, [1, 1, 0, 10]),
        (753, [3, 0, 0, 30]),
    ]
)
def test_correct_data(coin: int, expected: list) -> None:
    assert get_coin_combination(coin) == expected


def test_wrong_input_case() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("14")
