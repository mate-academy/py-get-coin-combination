from app.main import get_coin_combination


def test_main_when_value_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_different_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
