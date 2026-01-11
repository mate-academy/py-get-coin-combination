import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (7, [2, 1, 0, 0]),
        (-10, [0, 1, 1, -1]),
        (-1, [4, 0, 2, -1]),
        (-2, [3, 0, 2, -1]),
        (-31, [4, 1, 1, -2]),
        (70, [0, 0, 2, 2]),
        (123, [3, 0, 2, 4]),
        (999, [4, 0, 2, 39]),
        (44, [4, 1, 1, 1])
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cent, expected_error",
    [
        ("10", TypeError),
        (bool, TypeError),
        (None, TypeError),
    ]
)
def test_type_error_get_coin_combination(
        cent: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cent)
