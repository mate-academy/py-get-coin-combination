from app.main import get_coin_combination


def test_should_return_0_when_cents_are_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_1_nickel_when_5_cents():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_1_penny_when_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_correct_number_of_dimes():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_correct_number_of_quarters():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_different_coin_combinations():
    assert get_coin_combination(17) == [2, 1, 1, 0]
