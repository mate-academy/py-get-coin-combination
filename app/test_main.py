from app.main import get_coin_combination


def test_should_return_all_types_of_coins():
    assert get_coin_combination(66) == [1, 1, 1, 2]
