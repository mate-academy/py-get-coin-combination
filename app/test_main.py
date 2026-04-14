from app.main import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_four_pennies():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_penny_and_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_two_nickels():
    assert get_coin_combination(10) == [0, 0, 1, 0]  # 1 dime, not 2 nickels


def test_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_mixed_dime_nickel_pennies():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_two_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_all_coin_types():
    # 41 cents = 1 quarter + 1 dime + 1 nickel + 1 penny
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_max_pennies_before_nickel():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickel_plus_pennies():
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_large_amount():
    # 99 cents = 3 quarters + 2 dimes + 0 nickels + 4 pennies
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_exact_quarter_multiple():
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_dime_and_nickel():
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_returns_list():
    result = get_coin_combination(10)
    assert isinstance(result, list)


def test_returns_four_elements():
    result = get_coin_combination(10)
    assert len(result) == 4


def test_no_negative_values():
    result = get_coin_combination(7)
    assert all(c >= 0 for c in result)
