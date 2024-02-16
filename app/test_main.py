import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (41,[1, 1, 1, 1]),
        (0, [0, 0, 0, 0])
    ],
)
def test_only_for_nickels(cents, expected):
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (999, [4, 0, 2, 39]),
        (6666, [1, 1, 1, 266]),
        (999999, [4, 0, 2, 39999]),
    ],
)
def test_for_large_cents(cents, expected):
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (100, [0, 0, 0, 4]),
        (350, [0, 0, 0, 14]),
        (950, [0, 0, 0, 38]),
    ],
)
def test_only_for_quarters(cents, expected):
    assert get_coin_combination(cents) == expected
