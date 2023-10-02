import pytest


from app.main import get_coin_combination


def test_get_coin_combination_with_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_with_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_with_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_with_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_with_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
