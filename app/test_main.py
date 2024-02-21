from app.main import get_coin_combination
import pytest


def test_should_return_list_with_correct_values() -> None:
    assert get_coin_combination(18) == [3, 1, 1, 0]


def test_coins_is_positive() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)
