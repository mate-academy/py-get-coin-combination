import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount() -> None:
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_negative_amount() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-6)


def test_string_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")


def test_float_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(1.1)
