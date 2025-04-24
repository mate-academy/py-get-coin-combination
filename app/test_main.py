from app.main import get_coin_combination


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_1_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_1_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_1_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_1_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_big_number() -> None:
    assert get_coin_combination(1452) == [2, 0, 0, 58]


def test_all_numbers_used() -> None:
    assert get_coin_combination(66) == [1, 1, 1, 2]


def test_not_int() -> None:
    assert get_coin_combination
