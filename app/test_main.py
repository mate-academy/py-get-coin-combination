# tests/test_coin_combination.py
import pytest
from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_multiple_coins() -> None:
    assert get_coin_combination(37) == [2, 0, 1, 1]


def test_large_number_cents() -> None:
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_edge_case_99_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_another_multiple_coins() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_another_multiple_coins_16() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_another_multiple_coins_49() -> None:
    assert get_coin_combination(49) == [4, 0, 2, 1]


def test_another_multiple_coins_119() -> None:
    assert get_coin_combination(119) == [4, 1, 1, 4]


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (37, [2, 0, 1, 1]),
        (123, [3, 0, 2, 4]),
        (99, [4, 0, 2, 3]),
        (11, [1, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (49, [4, 0, 2, 1]),
        (119, [4, 1, 1, 4]),
    ],
)
def test_coin_combinations_parametrized(cents: int,
                                        expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
