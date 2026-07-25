import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (-5, ValueError),
        ("a", TypeError),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    if isinstance(expected, type) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            get_coin_combination(cents)
    else:
        assert get_coin_combination(cents) == expected
