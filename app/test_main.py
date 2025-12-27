from app.main import get_coin_combination


def test_e() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_3() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
