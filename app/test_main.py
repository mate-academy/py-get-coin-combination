from app.main import get_coin_combination


def test_should_return_correct_value():
    coins = get_coin_combination(17)
    assert coins == [2, 1, 1, 0]


def test_should_return_zeros_when_cents_equal_0():
    coins = get_coin_combination(0)
    assert coins == [0, 0, 0, 0]
