import pytest
from app.main import get_coin_combination


def test_value_should_raise_type_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")
        get_coin_combination(100.00)


def test_should_return_zeros_if_value_is_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_only_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_should_return_only_quarters() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_should_return_all_types_of_cents() -> None:
    assert get_coin_combination(117) == [2, 1, 1, 4]
    assert get_coin_combination(66) == [1, 1, 1, 2]
