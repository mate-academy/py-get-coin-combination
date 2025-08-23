from app.main import get_coin_combination


def test_get_coin_combination():
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(23) == [3, 0, 2, 0]
    assert get_coin_combination(15) == [0, 1, 1, 0]
    assert get_coin_combination(26) == [1, 0, 0, 1]

            