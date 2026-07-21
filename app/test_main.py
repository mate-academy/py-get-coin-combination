import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_combination",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test_given_0_cents"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test_return_only_pennies"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="test_return_only_nickels"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="test_return_only_dimes"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="test_return_only_quarters"
        ),
        pytest.param(
            68,
            [3, 1, 1, 2],
            id="test_return_all_coins"
        )
    ]
)
def test_get_coin_combination(
    cents: int,
    expected_combination: list
) -> None:
    arr = get_coin_combination(cents)
    assert arr == expected_combination
