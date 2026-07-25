import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result


@pytest.mark.parametrize(
    "coins, expected_error",
    [
        ("12", TypeError),
        ([12], TypeError)
    ]
)
def test_get_coin_combination_for_error(
        coins: int,
        expected_error: Exception
) -> None:
    with pytest.raises(Exception):
        get_coin_combination(coins)
