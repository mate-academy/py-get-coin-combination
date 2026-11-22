import pytest
from app.main import get_coin_combination


def get_correct_coins(coins: int) -> tuple[int, list[int]]:
    coins_combination = [0, 0, 0, 0]
    coins_combination[3] += coins // 25
    remainder = coins % 25
    coins_combination[2] += remainder // 10
    remainder = remainder % 10
    coins_combination[1] += remainder // 5
    remainder = remainder % 5
    coins_combination[0] += remainder
    return coins, coins_combination


@pytest.mark.parametrize(
    "cents, expected",
    [get_correct_coins(i) for i in range(10)]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
