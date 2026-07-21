from app.main import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]

def test_only_pennies():
    assert get_coin_combination(3) == [3, 0, 0, 0]

def test_only_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]

def test_only_dimes():
    assert get_coin_combination(20) == [0, 0, 2, 0]

def test_only_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]

def test_combination_quarters_and_dimes():
    assert get_coin_combination(65) == [0, 0, 1, 2]

def test_combination_all_coins():
    assert get_coin_combination(41) == [1, 1, 1, 1]  # 1 penny, 1 nickel, 1 dime, 1 quarter

def test_large_amount():
    assert get_coin_combination(99) == [4, 0, 2, 3]  # 4 pennies, 0 nickels, 2 dimes, 3 quarters
