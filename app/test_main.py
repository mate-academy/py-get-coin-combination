from app.main import get_coin_combination


def test_when_only_a_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_when_only_a_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_when_only_pennies_and_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_when_only_a_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_when_only_pennies_and_nickels_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def when_only_a_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def when_all_the_coins() -> None:
    assert get_coin_combination(42) == [2, 1, 1, 1]
