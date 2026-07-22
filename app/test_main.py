from app.main import get_coin_combination


def test_when_given_1_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_when_2_coins_are_given() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_when_17_coins_are_given() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_when_given_50_coins() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
