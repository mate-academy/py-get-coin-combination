import pytest


from app.main import get_coin_combination


def test_get_coin_combination_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_large_amount() -> None:
    assert get_coin_combination(9999) == [4, 0, 2, 399]


def test_get_coin_combination_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("gogo")
