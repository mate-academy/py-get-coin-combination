from app.main import get_coin_combination


def test_get_coin_combination_when_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_when_one_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_when_one_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_when_one_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_when_combination_of_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_when_large_amount() -> None:
    assert get_coin_combination(93) == [3, 1, 1, 3]
