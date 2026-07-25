from app.main import get_coin_combination

def test_one_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents():
    assert get_coin_combination(6) == [1, 1, 0, 0]
