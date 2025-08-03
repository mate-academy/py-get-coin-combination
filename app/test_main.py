from app.main import get_coin_combination


def test_zero_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cent() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cent() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifteen_cent() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
