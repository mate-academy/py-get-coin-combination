import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
    ]
)
def test_get_coin_combination(value: int, expected: list) -> None:
    assert get_coin_combination(value) == expected
