import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "current, expected_value",
    [
        (1, [1, 0, 0, 0]),
        (0, [0, 0, 0, 0]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        ("str", TypeError)
    ],
    ids=[
        "if 1 must be only 1 cent",
        "must be zero if input zero",
        "test for all coins",
        "if 50 must be 2 quarters",
        "str must raise TypeError"
    ]
)
def test_get_coin_combination(
        current: int,
        expected_value: list | TypeError) -> None:
    if (isinstance(expected_value, type)
            and issubclass(expected_value, Exception)):
        with pytest.raises(expected_value):
            get_coin_combination(current)
    else:
        assert get_coin_combination(current) == expected_value
