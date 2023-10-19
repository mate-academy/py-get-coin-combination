from app.main import get_coin_combination


# write your tests here
def test_get_coin_combination_quarter():
    value = 25
    expected = [0, 0, 0, 1]
    result = get_coin_combination(value)
    assert result == expected


def test_get_coin_combination_return_nickel():
    value = 5
    expected = [0, 1, 0, 0]
    result = get_coin_combination(value)
    assert result == expected


def test_get_coin_dime():
    value = 10
    expected = [0, 0, 1, 0]
    result = get_coin_combination(value)
    assert result == expected


def test_get_coin_combination_returns_different_coins():
    value = 66
    result = get_coin_combination(value)
    assert all(result[i] > 0 for i in range(1, 4))