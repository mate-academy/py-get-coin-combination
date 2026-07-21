from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_type_and_length() -> None:
    """Check that the function returns list of length 4 with integers."""
    result: list[int] = get_coin_combination(42)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
