import pytest

from app.main import get_coin_combination


def test_type_data_argument() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("string")


def test_type_data_argument2() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_penni() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
