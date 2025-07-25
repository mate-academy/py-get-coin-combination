from app.main import get_coin_combination


def test_return_lisr_of_zeroes_if_input_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_list_of_ones_if_input_41():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_return_quarters_if_input_75():
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_return_dimes_if_input_20():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_return_nickel_if_input_5():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_penny_if_input_4():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_return_zeros_if_input_lesser_0():
    assert get_coin_combination(-5) == [0, 0, 0, 0]
