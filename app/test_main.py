import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins_count",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test should return list with length 4"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test should work correctly with zero value"
        ),
        pytest.param(
            99,
            [4, 0, 2, 3],
            id="test should work correctly with different coins values"
        ),
        pytest.param(
            6890,
            [0, 1, 1, 275],
            id="test should work correctly with big value"
        ),
    ]
)
def test_should_calculate_smallest_coin_count(
        cents: int,
        coins_count: list
) -> None:
    assert get_coin_combination(cents) == coins_count
