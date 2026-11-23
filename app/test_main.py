from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_coins_list",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="should return zeros if cents = 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should add only pennies if cents < 5"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="should add nickels if cents >= 5"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should add nickels if cents >= 5"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should add dimes if cents >= 10"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should add dimes if cents >= 10"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="should add quarters if cents >= 25"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should add quarters if cents >= 25"
        ),
        pytest.param(
            169, [4, 1, 1, 6],
            id="should add quarters if cents >= 25"
        ),
    ]
)
def test_get_coin_combination(
        cents: int,
        expected_coins_list: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_coins_list
