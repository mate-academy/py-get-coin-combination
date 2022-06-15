from app.main import get_coin_combination


def test_combination_should_be_zero():
    money = get_coin_combination(0)
    assert money == [0, 0, 0, 0]


def test_combination_should_be_one_penny():
    money = get_coin_combination(1)
    assert money == [1, 0, 0, 0]


def test_combination_should_be_one_penny_and_one_nickel():
    money = get_coin_combination(6)
    assert money == [1, 1, 0, 0]


def test_combination_should_be_two_pennies_nickel_and_dime():
    money = get_coin_combination(17)
    assert money == [2, 1, 1, 0]


def test_combination_should_be_two_quarters():
    money = get_coin_combination(50)
    assert money == [0, 0, 0, 2]
