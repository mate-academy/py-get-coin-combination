from app.coin_combination import get_coin_combination


def test_nothing_to_combine():
    goals = get_coin_combination(0)
    assert goals == [0, 0, 0, 0]


def test_nickels_may_be_confused_with_pennies():
    goals = get_coin_combination(65)
    assert goals == [0, 1, 1, 2]


def test_dimes_may_be_confused_with_nickles():
    goals = get_coin_combination(47)
    assert goals == [2, 0, 2, 1]


def test_quarters_may_be_confused_with_dimes():
    goals = get_coin_combination(80)
    assert goals == [0, 1, 0, 3]


def test_different_values():
    goals = get_coin_combination(99)
    assert goals == [4, 0, 2, 3]

    goals = get_coin_combination(68)
    assert goals == [3, 1, 1, 2]
