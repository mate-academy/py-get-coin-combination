from app.main import get_coin_combination


def test_should_check_all_coins() -> None:
    assert get_coin_combination(66) == [1, 1, 1, 2]


def test_should_check_zero_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
