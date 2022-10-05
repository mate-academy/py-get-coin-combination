from app.main import get_coin_combination


def test_return_zero_when_input_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_pennies_when_input_less_then_6():
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_return_nickels_when_input_more_then_6_and_less_10():
    assert get_coin_combination(8) == [3, 1, 0, 0]


def test_return_dimes_when_input_more_then_ten_and_less_25():
    assert get_coin_combination(21) == [1, 0, 2, 0]


def test_return_quarters_when_input_more_then_25():
    assert get_coin_combination(56) == [1, 1, 0, 2]
