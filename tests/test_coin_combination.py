from app.coin_combination import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_correct_determine_pennies():
    assert get_coin_combination(2) == [2, 0, 0, 0]


def test_correct_determine_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_correct_determine_dimes():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_correct_determine_quarters():
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_mixed_combination():
    assert get_coin_combination(93) == [3, 1, 1, 3]
