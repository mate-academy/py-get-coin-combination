from app.main import get_coin_combination


def test_when_got_zero_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_when_got_equivalent_coin_to_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_when_got_equivalent_coin_to_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_when_got_equivalent_coin_to_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
