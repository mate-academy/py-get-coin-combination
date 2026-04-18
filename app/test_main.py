import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (77, [2, 0, 0, 3])
    ]
)
def test_method_returns_smallest_coin_combination(
        cents: int,
        expected_result: list[int]
) -> None:
    result = get_coin_combination(cents)
    assert result == expected_result, \
        f"Expected: {expected_result}, got: {result}"
