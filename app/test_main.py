from app.main import get_coin_combination


def test_coins_eq_to_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_check_examples() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(30) == [0, 1, 0, 1]
    assert get_coin_combination(11) == [1, 0, 1, 0]
    assert get_coin_combination(15) == [0, 1, 1, 0]
    assert get_coin_combination(21) == [1, 0, 2, 0]


def test_check_big_numbers() -> None:
    assert get_coin_combination(4325456462) == [2, 0, 1, 173018258]


def test_check_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_check_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_check_quarter() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
