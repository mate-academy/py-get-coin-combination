import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result


def test_get_coin_combination_with_negative_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_get_coin_combination_with_no_integer_value() -> None:
    with pytest.raises(TypeError):
        get_coin_combination([1])
