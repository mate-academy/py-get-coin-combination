import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, expected",
    [

        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (25065, [0, 1, 1, 1002]),
    ],
    ids=[
        "zero_cent_output_0",
        "4_cents_output_4_penny",
        "5_cents_output_1_nickel",
        "5_cents_output_1_nickel_1_penny",
        "10_cents_output_1_dime",
        "16_cents_output_1_dime_1_nickel_1_penny",
        "25_cents_output_1_quarter",
        "30_cents_output_1_quarter_1_nickel",
        "41_cents_output_1_quarter_1_dime_1_nickel_1_penny",
        "big_amount_cents_output_1002_quarter_1_dime_1_nickel_0_penny",
    ]
)
def test_get_coin_combination(cent: int, expected: list) -> None:
    assert get_coin_combination(cent) == expected, (
        f"Function 'get_human_age' should return {expected} "
        f"when cents equal to {cent}"
    )
