from typing import Any

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, combination",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return one pennies"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return pennies and nickels"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return pennies, nickels and dimes"
        ),
        pytest.param(
            67,
            [2, 1, 1, 2],
            id="should return pennies, nickels dimes and quarters"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="should return only quarters"
        ),
    ]
)
def test_correct_combination(
        coins: int,
        combination: list[int]
) -> None:
    assert get_coin_combination(coins) == combination


@pytest.mark.parametrize(
    "coins, error",
    [
        pytest.param(
            "1",
            TypeError,
            id="should raise error when parameter is not int"
        ),
    ]
)
def test_raising_errors_correctly(
        coins: int,
        error: Any
) -> None:
    with pytest.raises(error):
        assert get_coin_combination(coins)
