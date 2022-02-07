from app.coin_combination import get_coin_combination


def test_nothing_to_combine():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_nickels_and_pennies():
    assert get_coin_combination(65) == [0, 1, 1, 2]


def test_dimes_and_nickles():
    assert get_coin_combination(47) == [2, 0, 2, 1]


def test_quarters_and_dimes():
    assert get_coin_combination(80) == [0, 1, 0, 3]


def test_different_values():
    assert get_coin_combination(99) == [4, 0, 2, 3]

    assert get_coin_combination(68) == [3, 1, 1, 2]
