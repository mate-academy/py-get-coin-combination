from app.main import get_coin_combination


def test_when_amount_is_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_if_coins_only_penny():
    assert get_coin_combination(2) == [2, 0, 0, 0]


def test_coins_with_nickel():
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_coins_with_dimes():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_coins_with_quarters():
    assert get_coin_combination(56) == [1, 1, 0, 2]


def test_should_return_all_type_coins():
    assert get_coin_combination(41) == [1, 1, 1, 1]
