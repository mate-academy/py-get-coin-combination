import app.main as main


def test_zero():
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies():
    assert main.get_coin_combination(3) == [3, 0, 0, 0]


def test_only_nickels():
    assert main.get_coin_combination(5) == [0, 1, 0, 0]


def test_only_dimes():
    assert main.get_coin_combination(10) == [0, 0, 1, 0]


def test_only_quarters():
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_pennies_and_nickels():
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_pennies_nickels_and_dimes():
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_nickels_and_quarters():
    assert main.get_coin_combination(30) == [0, 1, 0, 1]


def test_all_coin_types():
    # 41 = 25 + 10 + 5 + 1
    assert main.get_coin_combination(41) == [1, 1, 1, 1]


def test_minimal_number_of_coins():
    # 20 must be 2 dimes, not 4 nickels
    assert main.get_coin_combination(20) == [0, 0, 2, 0]


def test_complex_amount():
    # 99 = 3 quarters + 2 dimes + 4 pennies
    assert main.get_coin_combination(99) == [4, 0, 2, 3]
