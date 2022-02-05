import pytest
from app.coin_combination import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coin_combination",
    [
        (0, [0, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (18, [3, 1, 1, 0]),
        (72, [2, 0, 2, 2]),
    ]
)
def test_coin_combination_is_correct(cents, expected_coin_combination):
    assert get_coin_combination(cents) == expected_coin_combination
