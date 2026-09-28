from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_basic_cases(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_cents_is_positive() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_cents_is_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")
