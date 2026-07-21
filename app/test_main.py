from app.main import get_coin_combination


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_mixed_41() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_get_coin_combination_mixed_99() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_large_value() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
