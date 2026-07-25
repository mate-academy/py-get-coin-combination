import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 cent with coin 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 6 cent with coin 1, 5"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 17 cent with coin 1, 1, 5, 10"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 50 cent with coin 25, 25"
        ),
    ]
)
def test_coin_combination_correctly(cents: int, expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
