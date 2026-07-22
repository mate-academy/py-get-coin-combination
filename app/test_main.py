import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,expected_result",
    [
        pytest.param(
            17, [2, 1, 1, 0],
            id="should_check_returning_different_coins"
        ),
        pytest.param(
            42, [2, 1, 1, 1],
            id="should_check_returning_different_coins"
        )
    ]
)
def test_should_check_returning_different_coins(
        coins: int,
        expected_result: list
) -> None:
    assert get_coin_combination(coins) == expected_result
