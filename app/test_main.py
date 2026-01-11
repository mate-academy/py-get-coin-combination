from app.main import get_coin_combination


def test_get_one_nickel():
    coins = 41

    value = get_coin_combination(coins)

    assert value == [1, 1, 1, 1]
