from app.main import get_coin_combination


def test_should_return_correct_list_when_cents_equal_50():
    assert get_coin_combination(68) == [3, 1, 1, 2]
