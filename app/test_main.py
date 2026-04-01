from app.main import get_coin_combination


def test_number_coins_penny() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_number_coins_penny_and_nickel() -> None:
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_number_coins_penny_and_nickel_and_dime() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_number_coins_penny_and_nickel_and_dime_and_quarters() -> None:
    assert get_coin_combination(83) == [3, 1, 0, 3]
