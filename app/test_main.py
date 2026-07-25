import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (18, [3, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (79, [4, 0, 0, 3]),
        (67, [2, 1, 1, 2])
    ]
)
def test_function_get_different_numbers(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
