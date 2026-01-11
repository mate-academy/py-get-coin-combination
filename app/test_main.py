import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins_list",
    [(168, [168 % 25 % 10 % 5 // 1, 168 % 25 % 10 // 5,
            168 % 25 // 10, 168 // 25])])
def test_get_coin_combination(cents: int, coins_list: list) -> None:
    assert get_coin_combination(cents) == coins_list
