import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
        (65, [0, 1, 1, 2]),
        (20, [0, 0, 2, 0]),
        (5, [0, 1, 0, 0]),
        (117, [2, 1, 1, 4])
    ]
)
def test_get_coin_combination_calculate_correctly(cents, expected): # noqa
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "coins,expected",
    [
        ("0", TypeError),
        ([0], TypeError)
    ]
)
def test_get_coin_combination_raise_correct_errors(coins, expected): # noqa
    with pytest.raises(expected):
        get_coin_combination(coins)
