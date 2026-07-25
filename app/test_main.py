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
        (119, [4, 1, 1, 4])
    ]
)
def test_get_coin_combination_returns_correct_list(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected
