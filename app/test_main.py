import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "count_of_coins,expected_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (120, [0, 0, 2, 4]),
        (41, [1, 1, 1, 1])
    ]
)
def test_get_coin_combination(count_of_coins: int,
                              expected_combination: list[int]) -> None:
    assert get_coin_combination(count_of_coins) == expected_combination
