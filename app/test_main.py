from typing import List
from app import get_coin_combination


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], "Failed for 1 cent"


def test_single_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0], "Failed for 5 cents"


def test_single_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0], "Failed for 10 cents"


def test_single_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1], "Failed for 25 cents"


def test_combination_of_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0], "Failed for 6 cents"
    assert get_coin_combination(17) == [2, 1, 1, 0], "Failed for 17 cents"
    assert get_coin_combination(50) == [0, 0, 0, 2], "Failed for 50 cents"


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0], "Failed for 0 cents"


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3], "Failed for 99 cents"
    assert get_coin_combination(123) == [3, 0, 2, 4], "Failed for 123 cents"


def test_edge_cases() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0], "Failed for 4 cents"
    assert get_coin_combination(9) == [4, 1, 0, 0], "Failed for 9 cents"
    assert get_coin_combination(24) == [4, 0, 2, 0], "Failed for 24 cents"
