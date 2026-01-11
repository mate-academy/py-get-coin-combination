from app.main import get_coin_combination


def test_should_return_zeros_with_zero_input():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_four_cents():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_nine_cents():
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_should_return_eleven_cents():
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_should_return_twenty_five_cents():
    assert get_coin_combination(25) == [0, 0, 0, 1]
