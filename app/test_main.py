import pytest


from app.main import get_coin_combination


def test_get_coin_combination_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_11_cents() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_get_coin_combination_26_cents() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
