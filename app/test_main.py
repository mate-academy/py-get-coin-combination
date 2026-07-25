from app.main import get_coin_combination


def test_different_coins_not_only_pennies() -> None:
    cents = 17
    assert get_coin_combination(cents) == [2, 1, 1, 0]
