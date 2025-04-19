from app.main import get_coin_combination
import pytest


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_single_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_single_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_single_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_consecutive_amounts() -> None:
    assert get_coin_combination(42) == [2, 1, 1, 1]
    assert get_coin_combination(43) == [3, 1, 1, 1]
    assert get_coin_combination(44) == [4, 1, 1, 1]
    assert get_coin_combination(45) == [0, 0, 2, 1]


def test_negative_amount() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)
