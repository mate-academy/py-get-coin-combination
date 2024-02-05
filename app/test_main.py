from app.main import get_coin_combination


def test_return_expected_coins() -> None:
    coins = get_coin_combination(6)
    assert coins == [1, 1, 0, 0]


def test_return_zero_coins() -> None:
    coins = get_coin_combination(0)
    assert coins == [0, 0, 0, 0]
