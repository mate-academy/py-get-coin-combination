import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [(1, [1, 0, 0, 0]),
     (6, [1, 1, 0, 0]),
     (17, [2, 1, 1, 0]),
     (50, [0, 0, 0, 2]),
     (0, [0, 0, 0, 0])
     ])
def test_get_coin_combination_with_different_amounts(
    cents: int,
    expected: list,
) -> None:
    assert expected == get_coin_combination(cents)
