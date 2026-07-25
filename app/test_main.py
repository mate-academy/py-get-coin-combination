from app.main import get_coin_combination


def test_is_list() -> None:
    coins = get_coin_combination(5)

    assert isinstance(coins, list)


def test_numbers_of_pennies_less_5() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_numbers_of_pennies_nickels() -> None:
    coins = get_coin_combination(6)

    assert coins == [1, 1, 0, 0]


def test_numbers_of_pennies_dimes() -> None:
    coins = get_coin_combination(17)

    assert coins == [2, 1, 1, 0]


def test_numbers_of_pennies_quarters() -> None:
    coins = get_coin_combination(50)

    assert coins == [0, 0, 0, 2]


def test_numbers_of_pennies_zero() -> None:
    coins = get_coin_combination(0)

    assert coins == [0, 0, 0, 0]


def test_get_coin_combination_large_number() -> None:
    assert get_coin_combination(1234) == [4, 1, 0, 49]
