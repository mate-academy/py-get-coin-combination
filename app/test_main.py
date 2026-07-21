import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (7, [2, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (167, [2, 1, 1, 6])
    ],

)
def test_coin_combination_correctly(
        cents: int,
        expected_result: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_result
