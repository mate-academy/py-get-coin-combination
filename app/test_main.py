import pytest

from app.main import get_coin_combination


def test_normal() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_type_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("28")
