from app.main import get_coin_combination
import pytest


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination(
    cents: int,
    expected: list,
) -> None:
    assert get_coin_combination(cents) == expected
