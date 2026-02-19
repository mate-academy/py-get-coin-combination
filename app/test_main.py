import pytest
from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    result = main.get_coin_combination(cents)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 4, "Result should have 4 elements"
    assert result == expected, \
        (f"For cents: {cents}, "
         f"expected: {expected}, "
         f"got result: {result}")
