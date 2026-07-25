import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_valid_cases(
    cents: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_should_raise_for_negative_values() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-5)


def test_get_coin_combination_should_raise_for_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("10")
