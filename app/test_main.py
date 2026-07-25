from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins,expected_array",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return [1, 0, 0, 0]"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return [1, 1, 0, 0]"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return  [2, 1, 1, 0]"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return [0, 0, 0, 2]"
        )
    ]
)
def test_count_coins(coins: int, expected_array: list) -> None:
    assert get_coin_combination(coins) == expected_array
