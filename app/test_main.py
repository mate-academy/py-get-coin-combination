import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (40, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (829, [4, 0, 0, 33])
    ]
)
def test_check_coin_combination(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected
