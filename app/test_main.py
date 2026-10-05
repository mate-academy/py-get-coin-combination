import pytest
from app.main import get_coin_combination

# write your tests here


def test_number_of_cents_is_positive() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_negative_cents_raise_value_error() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_get_coin_combination_returns_list() -> None:
    result = get_coin_combination(50)
    assert isinstance(result, list), "Expected a list as the return type"
