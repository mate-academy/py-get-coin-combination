import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (68, [3, 1, 1, 2])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1018, [3, 1, 1, 40]),
        (222222, [2, 0, 2, 8888])
    ]
)
def test_get_coin_combination_edge_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
