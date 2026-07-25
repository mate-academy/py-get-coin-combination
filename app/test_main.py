from app.main import get_coin_combination


def test_zeroes() -> None:
    goals = get_coin_combination(0)
    assert goals == [0, 0, 0, 0]


def test_single_coins() -> None:
    goals = get_coin_combination(1)
    assert goals == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    goals = get_coin_combination(6)
    assert goals == [1, 1, 0, 0]


def test_pennies_nickels_dime() -> None:
    goals = get_coin_combination(17)
    assert goals == [2, 1, 1, 0]


def test_only_quarters() -> None:
    goals = get_coin_combination(50)
    assert goals == [0, 0, 0, 2]
