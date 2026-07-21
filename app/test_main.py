from app.main import get_coin_combination


def test_with_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_with_one() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_with_more_than_five() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_nickel_and_dime() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_with_all_coins() -> None:
    assert get_coin_combination(169) == [4, 1, 1, 6]


def test_with_quarter() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
