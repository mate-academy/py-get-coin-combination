import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value, coins",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
        (67, [2, 1, 1, 2]),
    ]
)
def test_get_coin_combination(value: int, coins: list) -> None:
    assert (
        get_coin_combination(value) == coins
    ), f"Wrong coin combination: {value}"
