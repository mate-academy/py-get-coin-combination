from app.main import get_coin_combination


def test_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_complex() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_multiple_pennies() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_multiple_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_multiple_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_multiple_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_return_different_coins() -> None:
    result = get_coin_combination(6)
    assert result[0] > 0 and result[1] > 0


def test_return_multiple_types() -> None:
    result = get_coin_combination(17)
    assert result[0] > 0 and result[1] > 0 and result[2] > 0
