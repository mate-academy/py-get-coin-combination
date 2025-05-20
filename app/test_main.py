from app.main import get_coin_combination


def test_get_coin_combination_return_0_when_given_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]

def test_get_coin_combination_return_1_of_each_currency_given_41():
    assert get_coin_combination(41) == [1, 1, 1, 1]