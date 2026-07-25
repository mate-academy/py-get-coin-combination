import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (3, [3, 0, 0, 0]),
        (7, [2, 1, 0, 0]),
        (22, [2, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_coin_combination(
        cents: int,
        expected_combination: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_combination
