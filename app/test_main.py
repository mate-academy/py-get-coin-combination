from app.main import get_coin_combination


def test_type_correct_return_result():
    assert isinstance(get_coin_combination(20), list)


def test_when_give_zero_and_return_all_zero_list():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_return_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_one_penny_plus_one_nikel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_one_penny_plus_one_nikel_plus_one_dime():
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_one_penny_plus_one_nikel_plus_one_dime_plus_one_quarter():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_separt_coins_for_big_amount():
    assert get_coin_combination(1134) == [4, 1, 0, 45]
