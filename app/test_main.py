from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (100, [0, 0, 0, 4]),
        (99, [4, 0, 2, 3]),
        (1111, [1, 0, 1, 44])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_gtc_should_take_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(10.6)
    with pytest.raises(TypeError):
        get_coin_combination("1")

def test_gtc_should_take_positive_int() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-8)
