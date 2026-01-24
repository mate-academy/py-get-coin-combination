from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins, expected_combination",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="0 coins"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="is equal to 1 penny "
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="is equal to 1 nickel"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="is equal to 1 dime"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="is equal to 1 quarter"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="is equal to 1 quarter, dime, nickel and penny"
        ),
    ]
)
def test_get_right_combination(coins: int,
                               expected_combination: list[int]) -> None:
    assert (
        get_coin_combination(coins) == expected_combination
    ), f"{coins} coin(s) should give {expected_combination} combination"
