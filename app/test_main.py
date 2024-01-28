from app.main import get_coin_combination


def test_valid_arguments() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_different_coins() -> None:
    assert get_coin_combination(294) == [4, 1, 1, 11]