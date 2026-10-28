from app import main


def test_return_only_pennies() -> None:
    assert main.get_coin_combination(3) == [3, 0, 0, 0]


def test_return_only_nickels() -> None:
    assert main.get_coin_combination(5) == [0, 1, 0, 0]


def test_return_only_dimes() -> None:
    assert main.get_coin_combination(10) == [0, 0, 1, 0]


def test_return_only_quarters() -> None:
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_return_combination_of_coins() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_return_quarters_and_nickels() -> None:
    assert main.get_coin_combination(30) == [0, 1, 0, 1]


def test_return_quarters_and_dimes() -> None:
    assert main.get_coin_combination(60) == [0, 0, 1, 2]


def test_return_two_quarters() -> None:
    assert main.get_coin_combination(50) == [0, 0, 0, 2]


def test_return_zero() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_return_combination_with_all_coins() -> None:
    assert main.get_coin_combination(41) == [1, 1, 1, 1]
