from app.main import get_coin_combination


def test_null_numbers_of_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_penny_quantity() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickel_quantity() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_dimes_quantity() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_quarter_quantity() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_big_amount_of_coins() -> None:
    assert get_coin_combination(117) == [2, 1, 1, 4]
