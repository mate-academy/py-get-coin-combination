from app.main import get_coin_combination


def test_if_input_data_is_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_if_input_data_is_aliquot_10():
    assert get_coin_combination(40) == [0, 1, 1, 1]


def test_when_result_include_all_coins():
    assert get_coin_combination(68) == [3, 1, 1, 2]


def test_if_input_data_is_big_integer():
    assert get_coin_combination(137) == [2, 0, 1, 5]
