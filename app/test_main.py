import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number_of_coins,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(number_of_coins: int,
                              expected_result: list[int]) -> None:
    assert get_coin_combination(number_of_coins) == expected_result
