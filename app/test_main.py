from app.main import get_coin_combination


def test_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_6_coin() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_17_coin() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_50_coin() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
