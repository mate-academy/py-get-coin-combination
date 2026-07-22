from app.main import get_coin_combination


def test_zero_checker() -> None:
    assert get_coin_combination(False) == [0, 0, 0, 0]


def test_different_types_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
