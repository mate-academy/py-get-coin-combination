from app.main import get_coin_combination


def test_should_return_only_pennies_if_value_less_than_5():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_of_each_coin():
    assert get_coin_combination(41) == [1, 1, 1, 1]
