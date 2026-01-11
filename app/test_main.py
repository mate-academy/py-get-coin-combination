from app.main import get_coin_combination


def test_conversion() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_borders() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_min_coins() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
