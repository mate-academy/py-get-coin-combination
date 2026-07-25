import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="zero_cents"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="one_penny"),
        pytest.param(
            5, [0, 1, 0, 0],
            id="one_nickel"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="one_dime"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="one_quarter"
        ),
        pytest.param(
            4, [4, 0, 0, 0],
            id="four_pennies"
        ),
        pytest.param(
            9, [4, 1, 0, 0],
            id="nine_cents_one_nickel_four_pennies"
        ),
        pytest.param(
            24, [4, 0, 2, 0],
            id="twenty_four_cents_two_dimes_four_pennies"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="all_coins_combination"
        ),
        pytest.param(
            99, [4, 0, 2, 3],
            id="large_combination"
        )
    ]
)
def test_get_coin_combination(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected
