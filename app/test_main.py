from app.main import get_coin_combination


def test_100_cents():
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_99_cents():
    assert get_coin_combination(99) == [4, 0, 2, 3]
