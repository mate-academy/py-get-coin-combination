from app.main import get_coin_combination


def test_coin_combination_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_coin_combination_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_coin_combination_penny_nickel_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_coin_combination_dime() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
