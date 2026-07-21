import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (3, [3, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (7, [2, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
    (2398, [3, 0, 2, 95]),
    (9999, [4, 0, 2, 399])
])


def test_various_combinations(cents, expected):
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("invalid_input, expected_exception", [
    (-5, ValueError),
    (-100, ValueError),
    (12.5, TypeError),
    ("100", TypeError),
    (None, TypeError),
])


def test_invalid_inputs(invalid_input, expected_exception):
    with pytest.raises(expected_exception):
        get_coin_combination(invalid_input)
