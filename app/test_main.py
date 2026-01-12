import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount_of_cents,expected_result",
    [
        pytest.param(
            75,
            [0, 0, 0, 3],
            id="should convert 75 into 3 quarters"
        ),
        pytest.param(
            20,
            [0, 0, 2, 0],
            id="should convert 20 into 2 dimes"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="should convert 5 into 1 nickels"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="should convert 4 into 4 pennies"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should convert 41 into all coin types"
        ),
    ]
)
def test_get_coin_combination(
        amount_of_cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(amount_of_cents) == expected_result
