from app.main import get_coin_combination


def test_should_return_right_result_when_cent_1_4():
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_should_return_right_result_when_cent_5_9():
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_should_return_right_result_when_cent_10_24():
    assert get_coin_combination(23) == [3, 0, 2, 0]


def test_should_return_right_result_when_cent_25_and_more():
    assert get_coin_combination(67) == [2, 1, 1, 2]
