from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "initial_coins, expected_coins",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="one cent equal one penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="five cents equal one nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="ten cents equal one dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="twenty five cents equal one quarter"
        )
    ]
)
def test_modify_coins_correctly(
        initial_coins: int,
        expected_coins: list
) -> None:
    assert get_coin_combination(initial_coins) == expected_coins
