from app.main import get_coin_combination


def test_should_return_correct_list_when_cents_equal_50():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_correct_list_when_cents_equal_100():
    assert get_coin_combination(50) == [0, 0, 0, 4]
