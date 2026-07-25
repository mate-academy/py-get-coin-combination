from app.main import get_coin_combination


def test_should_return_correct_value_when_cent_less_5():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_correct_value_when_cent_less_9():
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_should_return_correct_value_when_cent_less_25():
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_should_return_correct_value_when_cent_over_25():
    assert get_coin_combination(75) == [0, 0, 0, 3]
