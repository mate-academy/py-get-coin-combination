import pytest

from app.main import get_coin_combination


# write your tests here
def test_cannot_use_str_as_cents() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents="50")


def test_cannot_use_float_as_cents() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents=25.3)