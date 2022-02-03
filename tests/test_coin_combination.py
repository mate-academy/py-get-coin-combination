from app.coin_combination import get_coin_combination


def test_quarter():
    goals = get_coin_combination(25)

    assert goals[3] == 1


def test_dime():
    goals = get_coin_combination(10)

    assert goals[2] == 1


def test_nickel():
    goals = get_coin_combination(5)

    assert goals[1] == 1


def test_penny():
    goals = get_coin_combination(1)

    assert goals[0] == 1


def test_big_value():
    goals = get_coin_combination(46364)

    assert goals == [4, 0, 1, 1854]
