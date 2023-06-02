from app.main import get_coin_combination


def test_1_penny():
    assert(
        get_coin_combination(1) == [1, 0, 0, 0]
    ), "If 1 cents money should return zeros"


def test_6_penny():
    assert(
        get_coin_combination(6) == [1, 1, 0, 0]
    ), "If 6 cents should return 1 1 0 0"


def test_17_penny():
    assert(
        get_coin_combination(17) == [2, 1, 1, 0]
    ), "If 17 cents money should return 2 1 1 0"


def test_50_penny():
    assert(
        get_coin_combination(50) == [0, 0, 0, 2]
    ), "If 50 cents should return 0 0 0 2"
