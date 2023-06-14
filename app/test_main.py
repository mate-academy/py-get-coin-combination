import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="When 0 should return 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="When 1 should return 1 number"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="When 6 should return [1, 1, 0, 0]"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="When 17 should return [2, 1, 1, 0]"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="When 50 should return [0, 0, 0, 2]"
        ),
    ]
)
def test_coin_combination(cents: int, expected_coins: list[int]) -> None:
    assert get_coin_combination(cents) == expected_coins
