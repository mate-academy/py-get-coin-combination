from app.main import get_coin_combination


def test_get_coin_combination():
    assert get_coin_combination(41) == [1, 1, 1, 1]