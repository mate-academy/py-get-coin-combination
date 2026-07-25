from app.main import get_coin_combination
import pytest


def test_should_convert_correctly_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_convert_correctly_nickels() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_should_convert_correctly_dimes() -> None:
    assert get_coin_combination(19) == [4, 1, 1, 0]


def test_should_convert_correctly_quarters() -> None:
    assert get_coin_combination(44) == [4, 1, 1, 1]


def test_should_correctly_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("10")


def test_should_return_list() -> None:
    result = get_coin_combination(99)
    assert isinstance(result, list)


def test_get_human_age_with_zero_ages() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
