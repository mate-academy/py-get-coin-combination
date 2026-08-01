import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero_cent"),

        pytest.param(1, [1, 0, 0, 0], id="exact_penny"),
        pytest.param(5, [0, 1, 0, 0], id="exact_nickel"),
        pytest.param(10, [0, 0, 1, 0], id="exact_dime"),
        pytest.param(25, [0, 0, 0, 1], id="exact_quarter"),

        pytest.param(4, [4, 0, 0, 0], id="max_pennies_before_nickel"),
        pytest.param(9, [4, 1, 0, 0], id="max_coins_before_dime"),
        pytest.param(24, [4, 0, 2, 0], id="max_coins_before_quarter"),

        pytest.param(6, [1, 1, 0, 0], id="single_penny_and_nickel"),
        pytest.param(17, [2, 1, 1, 0], id="with_dime_nickel_pennies"),
        pytest.param(50, [0, 0, 0, 2], id="two_quarters"),
        pytest.param(99, [4, 0, 2, 3], id="large_combination_all_coin_types")
    ]
)
def test_should_return_correct_invalid(
        cents: int,
        expected_coins: list

) -> None:
    assert get_coin_combination(cents) == expected_coins
