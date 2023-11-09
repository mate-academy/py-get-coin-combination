import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, excepted",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (11, [1, 0, 1, 0]),
        (30, [0, 1, 0, 1])
    ]
)
def test_coin_combination_with_different_numbers(
        cents: int,
        excepted: list
) -> None:
    assert get_coin_combination(cents) == excepted
