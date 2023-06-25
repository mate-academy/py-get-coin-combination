import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ]
)
def test_should_return_correct_combination(
        coins: int,
        expected_combination: list[int]
) -> None:

    assert get_coin_combination(coins) == expected_combination
