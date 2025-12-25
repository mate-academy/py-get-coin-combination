from app.main import get_coin_combination


def test_with_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_with_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_with_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_with_quarter() -> None:
    assert get_coin_combination(43) == [3, 1, 1, 1]


def test_a_lot_of_money() -> None:
    assert get_coin_combination(816) == [1, 1, 1, 32]
