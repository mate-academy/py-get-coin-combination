from app.main import get_coin_combination


def test_get_coin_combination_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
