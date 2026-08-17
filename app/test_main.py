from app.main import get_coin_combination


def test_get_coin_combination_one() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_six() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_seventeen() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_fifty() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
