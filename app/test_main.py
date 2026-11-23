import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin_combination,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (67, [2, 1, 1, 2]),
    ]
)
def test_get_coin_combinations(coin_combination: int, expected: list) -> None:
    assert get_coin_combination(coin_combination) == expected
