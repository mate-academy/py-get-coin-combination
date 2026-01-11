import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins_amount,combination",
    [
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(16, [1, 1, 1, 0]),
        pytest.param(41, [1, 1, 1, 1])
    ]
)
def test_all_smallest_ranges(coins_amount: int, combination: list) -> None:
    assert get_coin_combination(coins_amount) == combination
