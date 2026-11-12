from __future__ import annotations

import pytest

from app.main import get_coin_combination


def test_one_cent_returns_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_five_cents_returns_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_ten_cents_returns_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_twenty_five_cents_returns_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_six_cents_returns_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents_returns_expected_combination() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents_returns_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents_returns_no_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_ninety_nine_cents_returns_expected_combination() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_one_hundred_cents_returns_four_quarters() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination_returns_expected_result(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected
