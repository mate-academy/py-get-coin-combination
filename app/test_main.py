from app.main import get_coin_combination


def test_get_one_nickel():
    coins = 0

    value = get_coin_combination(coins)

    assert value == [0, 0, 0, 0]

def test_get_one_penny():
    coins = 1

    value = get_coin_combination(coins)

    assert value == [1, 0, 0, 0]


def test_get_one_nickel():
    coins = 5

    value = get_coin_combination(coins)

    assert value == [0, 1, 0, 0]


def test_get_one_nickel():
    coins = 10

    value = get_coin_combination(coins)

    assert value == [0, 0, 1, 0]


def test_get_one_nickel():
    coins = 25

    value = get_coin_combination(coins)

    assert value == [0, 0, 0, 1]


def test_get_one_nickel():
    coins = 41

    value = get_coin_combination(coins)

    assert value == [1, 1, 1, 1]
