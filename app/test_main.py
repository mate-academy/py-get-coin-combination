from app.main import get_coin_combination

def test_coins_equals_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]

def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_one_penny_and_one_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]

def test_two_pennies_and_one_nickel_and_one_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]

def test_two_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]
