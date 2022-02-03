from app.coin_combination import get_coin_combination


def test_check_right_count_of_coins():
    assert get_coin_combination(17) == [2, 1, 1, 0]  # here we've checked pennies, nickels and dime
    assert get_coin_combination(50) == [0, 0, 0, 2]  # here quarters were checked


def test_check_zero_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]  # 0 cents
