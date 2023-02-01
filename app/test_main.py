from app.main import get_coin_combination


def test_one() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
