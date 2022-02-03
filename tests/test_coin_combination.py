from app.coin_combination import get_coin_combination


def test_type():
    assert type(get_coin_combination(0)) == list
    assert len(get_coin_combination(0)) == 4
    assert all(type(i) == int for i in get_coin_combination(0))


def test_limit_values():
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_lot_of_coins():
    assert get_coin_combination(516) == [1, 1, 1, 20]
    assert get_coin_combination(1043) == [3, 1, 1, 41]
