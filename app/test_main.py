import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [
        (0, [0, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),

    ]
)
def test_check_right_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result


def test_errors() -> None:
    with pytest.raises(TypeError):
        get_coin_combination()
