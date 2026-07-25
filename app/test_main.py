from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (250, [0, 0, 0, 10]),
        (-100, [0, 0, 0, -4]),
        (150, [0, 0, 0, 6]),
    ]
)
def test_value(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
