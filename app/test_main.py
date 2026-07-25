from app.main import get_coin_combination


def test_should_return_zeros_if_zero_given():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_if_less_6_given():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_nickel_if_more_6_less_10_given():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_dimes_if_more_10_less_25_given():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_quarters_if_more_25_given():
    assert get_coin_combination(50) == [0, 0, 0, 2]
