import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2]),
    ]
)
def test_returns_correct_coin_combination(
        coins: int,
        expected_result: list
) -> None:
    assert get_coin_combination(coins) == expected_result
