from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickels_and_pennies() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_dimes_nickels_pennies() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_quarters_and_other_coins() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_large_amounts() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(117) == [2, 1, 1, 4]
    assert get_coin_combination(199) == [4, 0, 2, 7]
    assert get_coin_combination(250) == [0, 0, 0, 10]
