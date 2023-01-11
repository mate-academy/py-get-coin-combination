from app.main import get_coin_combination


def test_return_only_one_type() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_return_different_coins() -> None:
    assert get_coin_combination(33) == [3, 1, 0, 1]