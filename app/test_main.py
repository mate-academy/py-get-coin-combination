from app.main import get_coin_combination


def test_number_of_pennies() -> None:
    assert get_coin_combination(1)[0] == 1


def test_number_of_nickels() -> None:
    assert get_coin_combination(5)[1] == 1


def test_number_of_dimes() -> None:
    assert get_coin_combination(10)[2] == 1


def test_number_of_quarters() -> None:
    assert get_coin_combination(25)[3] == 1


def test_coin_combination() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
