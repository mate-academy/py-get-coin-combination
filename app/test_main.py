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
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (75, [0, 0, 0, 3]),
        (4, [4, 0, 0, 0]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4])
    ]
)
def test_coin_combination_is_lowest_number_of_coins(
    cents: int,
    expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        (-1),
        (-300),
        (-12)
    ]
)
def test_value_error(cents: int) -> None:
    with pytest.raises(ValueError):
        assert get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [
        ("12"),
        (None),
        (True),
        ("twenty")
    ]
)
def test_type_error(cents: int) -> None:
    with pytest.raises(TypeError):
        assert get_coin_combination(cents)
