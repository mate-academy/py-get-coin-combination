import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (88, [3, 0, 1, 3])
    ]
)
def test_coin_combination(cent: int, expected: list) -> None:
    assert get_coin_combination(cent) == expected
