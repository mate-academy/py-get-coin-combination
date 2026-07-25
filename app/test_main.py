from app.main import get_coin_combination


def test_combination_for_0_cent():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_combination_for_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_combination_for_6_cents():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_combination_for_17_cents():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_combination_for_51_cents():
    assert get_coin_combination(51) == [1, 0, 0, 2]
