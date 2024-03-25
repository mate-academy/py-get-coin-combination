from app.main import get_coin_combination


def test_get_coin_combination():
    assert get_coin_combination(1) == [1, 0, 0, 0]  # 1 penny
    assert get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
    assert get_coin_combination(17) == [2, 1, 1, 0]  # 2 pennies + 1 nickel + 1 dime
    assert get_coin_combination(50) == [0, 0, 0, 2]  # 2 quarters

