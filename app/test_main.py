from app.main import get_coin_combination


def test_with_no_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_with_pennies():
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_with_pennies_and_nickles():
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_with_pennies_nickles_and_dimes():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_with_pennies_nickles_dimes_and_quarters():
    assert get_coin_combination(43) == [3, 1, 1, 1]
