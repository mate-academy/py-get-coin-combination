from app.coin_combination import get_coin_combination


def test_result_type_len_and_zero_value():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_result_by_one_coin_of_each_value():
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mix_of_coins():
    assert get_coin_combination(56) == [1, 1, 0, 2]
    assert get_coin_combination(23) == [3, 0, 2, 0]
    assert get_coin_combination(142) == [2, 1, 1, 5]
