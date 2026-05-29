import pytest

from app import main


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
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_should_return_correct_coin_combination(
    cents: int,
    expected: list,
) -> None:
    assert main.get_coin_combination(cents) == expected
