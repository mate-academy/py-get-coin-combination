from app.main import get_coin_combination


def test_should_return_when_cents_is_zero():
    coins = get_coin_combination(0)

    assert coins == [0, 0, 0, 0]


def test_should_return_expected_coins_only_penny():
    coins = get_coin_combination(1)

    assert coins == [1, 0, 0, 0]


def test_should_return_expected_coins_penny_nickel():
    coins = get_coin_combination(6)

    assert coins == [1, 1, 0, 0]


def test_should_return_expected_coins_penny_nickel_dime():
    coins = get_coin_combination(17)

    assert coins == [2, 1, 1, 0]


def test_should_return_expected_coins_quarters():
    coins = get_coin_combination(50)

    assert coins == [0, 0, 0, 2]
