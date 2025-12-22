import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (99, [4, 0, 2, 3]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (5, [0, 1, 0, 0]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_should_raise_exception_when_cents_not_int() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")
