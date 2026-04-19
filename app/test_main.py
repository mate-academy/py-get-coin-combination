from app.main import get_coin_combination


def test_should_return_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]

def test_return_only_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_six_cents():
    assert get_coin_combination(6) == [1, 1, 0, 0]

def test_seventeen_cents():
    assert get_coin_combination(17) == [2, 1, 1, 0]

def test_fifty_cents():
    assert get_coin_combination(50) == [0, 0, 0, 2]
