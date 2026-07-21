import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(coins: int, expected: list) -> None:
    result = get_coin_combination(coins)
    assert isinstance(result, list)
    assert len(result) == 4
    assert result == expected
