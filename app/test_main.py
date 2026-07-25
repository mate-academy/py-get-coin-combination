from app.main import get_coin_combination


def test_should_return_0_when_cents_are_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_1_when_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_when_1_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_1_when_1_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_1_when_1_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_correct_list_with_17_cents():
    assert get_coin_combination(17) == [2, 1, 1, 0]
