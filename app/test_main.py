from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_various_combinations(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_for_negative_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_for_non_integer_value() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")
