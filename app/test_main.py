import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_cents, output_result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (42, [2, 1, 1, 1]),
        (543, [3, 1, 1, 21])
    ],
    ids=[
        "return only pennies",
        "return only nickels",
        "return only dimes",
        "return only quarters",
        "return pennies and nickels",
        "return pennies, nickels and dimes",
        "return pennies, nickels, dimes and quarters",
        "return big number of pennies, nickels, dimes and quarters"
    ]
)
def test_coin_combination(
        input_cents: int,
        output_result: list[int, int, int, int]
) -> None:
    assert get_coin_combination(input_cents) == output_result
