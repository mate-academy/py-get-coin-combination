import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (3, [3, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (7, [2, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (17, [2, 1, 1, 0]),
    (35, [0, 0, 1, 1]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
    (2398, [3, 0, 2, 95]),
    (9999, [4, 0, 2, 399])
])
def test_various_combinations(cents, expected):
    assert get_coin_combination(cents) == expected


def test_large_amount():
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_negative_amount():
    with pytest.raises(ValueError):
        get_coin_combination(-5)


def test_non_integer_input():
    with pytest.raises(TypeError):
        get_coin_combination(12.5)
