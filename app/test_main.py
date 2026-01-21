from app.main import get_coin_combination


def test_with_zero_value() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_check_in_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_check_in_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_check_in_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_check_in_quart() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_check_all_conversion() -> None:
    assert get_coin_combination(68) == [3, 1, 1, 2]
