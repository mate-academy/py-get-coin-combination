from app.main import get_coin_combination


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_different_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_quarters_coins() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
