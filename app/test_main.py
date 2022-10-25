from app.main import get_coin_combination


def test_when_is_negative_should_convert_to_negative() -> None:
    assert get_coin_combination(-3) == [2, 0, 2, -1]


def test_when_is_zero_should_convert_to_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_convert_to_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_convert_to_pennies_and_nickels() -> None:
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_should_convert_to_pennies_nickels_and_dimes() -> None:
    assert get_coin_combination(19) == [4, 1, 1, 0]


def test_should_convert_to_pennies_nickels_dimes_and_quarters() -> None:
    assert get_coin_combination(57) == [2, 1, 0, 2]


def test_when_is_too_big_should_convert_to_all_coins() -> None:
    assert get_coin_combination(243) == [3, 1, 1, 9]
