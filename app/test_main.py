from app.main import get_coin_combination


def test_should_return_1_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_penny_and_1_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_1_penny_1_nickel_1_dime():
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_should_return_2_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]
