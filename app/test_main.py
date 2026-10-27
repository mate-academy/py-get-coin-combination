import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    """Test get_coin_combination with various amounts of cents."""
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        -1,
        -10,
    ],
)
def test_get_coin_combination_negative_raises_value_error(
    cents: int,
) -> None:
    """Test that negative cents raise ValueError."""
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [
        "10",
        None,
        10.5,
    ],
)
def test_get_coin_combination_invalid_type_raises_type_error(
    cents: int,
) -> None:
    """Test that invalid types raise TypeError."""
    with pytest.raises(TypeError):
        get_coin_combination(cents)
