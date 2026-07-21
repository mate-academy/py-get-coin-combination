import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coin_combination",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="get only pennies"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="get only nickels"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="get only dimes"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="get only quarters"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="get every coin"
        ),
    ]
)
def test_get_human_age(
        cents: int,
        expected_coin_combination: list
) -> None:
    assert get_coin_combination(cents) == expected_coin_combination
