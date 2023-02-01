import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "initial_coins, expected_coins",
    [
        (4, [4, 0, 0, 0]),
        (7, [2, 1, 0, 0]),
        (18, [3, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (57, [2, 1, 0, 2])
    ]
)
def test_correctly_conversion_coin_combination(
        initial_coins: int,
        expected_coins: list
) -> None:
    assert get_coin_combination(initial_coins) == expected_coins