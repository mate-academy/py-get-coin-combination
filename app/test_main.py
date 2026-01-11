from app.main import get_coin_combination


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0], "expect list [0, 0, 0, 0]"


def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0], "expect list [1, 0, 0, 0]"


def test_four_pennies():
    assert get_coin_combination(4) == [4, 0, 0, 0], "expect list [4, 0, 0, 0]"


def test_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0], "expect list [0, 1, 0, 0]"


def test_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0], "expect list [0, 0, 1, 0]"


def test_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1], "expect list [0, 0, 0, 1]"


def test_each_one():
    assert get_coin_combination(41) == [1, 1, 1, 1], "expect list [1, 1, 1, 1]"


def test_without_penny():
    assert get_coin_combination(40) == [0, 1, 1, 1], "expect list [0, 1, 1, 1]"


def test_all_cents():
    assert get_coin_combination(93) == [3, 1, 1, 3], "expect list [3, 1, 1, 3]"
