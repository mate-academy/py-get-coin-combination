from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_all_coins_type() -> None:
    assert get_coin_combination(66) == [1, 1, 1, 2]
