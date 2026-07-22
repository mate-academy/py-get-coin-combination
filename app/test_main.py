import pytest
from app.main import get_coin_combination


def test_should_raise_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15")


def test_calculate_correct() -> None:
    assert get_coin_combination(68) == [3, 1, 1, 2]
