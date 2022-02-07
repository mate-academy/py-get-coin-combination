from app.coin_combination import get_coin_combination


def test_should_return_zeros_if_cents_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_for_each_coin_in_list():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_return_right_result_for_big_number():
    assert get_coin_combination(994) == [4, 1, 1, 39]
