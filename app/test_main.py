from app import main


def test_zero_cents() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_only_penny() -> None:
    assert main.get_coin_combination(1) == [1, 0, 0, 0]


def test_only_nickel() -> None:
    assert main.get_coin_combination(5) == [0, 1, 0, 0]


def test_only_dime() -> None:
    assert main.get_coin_combination(10) == [0, 0, 1, 0]


def test_only_quarter() -> None:
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_penny_and_nickel() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_pennies_nickel_dime() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert main.get_coin_combination(50) == [0, 0, 0, 2]


def test_all_coin_types() -> None:
    assert main.get_coin_combination(41) == [1, 1, 1, 1]


def test_large_amount() -> None:
    assert main.get_coin_combination(99) == [4, 0, 2, 3]
