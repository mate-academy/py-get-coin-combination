from app.main import get_coin_combination


def test_when_no_money():
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


def test_one_nickel():
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test_one_penny():
    result = get_coin_combination(5)
    assert result == [0, 1, 0, 0]


def test_one_dime():
    result = get_coin_combination(10)
    assert result == [0, 0, 1, 0]


def test_one_quarter():
    result = get_coin_combination(25)
    assert result == [0, 0, 0, 1]


def test_change_all():
    result = get_coin_combination(66)
    assert result == [1, 1, 1, 2]
