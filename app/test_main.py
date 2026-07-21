import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (157, [2, 1, 0, 6]),
        (0, [0, 0, 0, 0]),
    ]
)
def test_values(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        ("121", TypeError),
        (tuple(), TypeError),
        (dict(), TypeError),
        (set(), TypeError),
        (complex(), TypeError),
    ]
)
def test_exceptions(
        cents: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
