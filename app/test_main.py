import pytest

from app.main import get_coin_combination


def test_get_coin_combination_returns_list() -> None:
    assert (
        isinstance(get_coin_combination(1), list)
    )


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (82, [2, 1, 0, 3])
    ]
)
def test_returns_correct_value(cents: int, expected: list) -> None:
    assert (
        get_coin_combination(cents) == expected
    )
