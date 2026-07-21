import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "specific_amount_of_coins,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(
    specific_amount_of_coins: int,
    expected_result: list
) -> None:
    assert get_coin_combination(specific_amount_of_coins) == expected_result
