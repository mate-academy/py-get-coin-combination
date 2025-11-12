import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_combination, test_id",
    [
        (1, [1, 0, 0, 0], "1_penny"),
        (6, [1, 1, 0, 0], "1_penny_1_nickel"),
        (17, [2, 1, 1, 0], "2_penny_1_nickel_1_dime"),
        (50, [0, 0, 0, 2], "example_2_quarters"),
        (0, [0, 0, 0, 0], "zero_cents"),
        (4, [4, 0, 0, 0], "max_pennies"),
        (99, [4, 0, 2, 3], "maximum_combination"),
        (5, [0, 1, 0, 0], "exact_nickel"),
        (10, [0, 0, 1, 0], "exact_dime"),
        (25, [0, 0, 0, 1], "exact_quarter"),
        (100, [0, 0, 0, 4], "exact_dollar"),
        (24, [4, 0, 2, 0], "mix_24_cents"),
        (7, [2, 1, 0, 0], "value_7_cents"),
    ],
    ids=[
        "1_penny",
        "1_penny_1_nickel",
        "2_penny_1_nickel_1_dime",
        "example_2_quarters",
        "zero_cents",
        "max_pennies",
        "maximum_combination",
        "exact_nickel",
        "exact_dime",
        "exact_quarter",
        "exact_dollar",
        "mix_24_cents",
        "value_7_cents",
    ]
)
def test_get_coin_combination_parametrized(
        cents: int,
        expected_combination: list[int],
        test_id: str
) -> None:
    assert get_coin_combination(cents) == expected_combination


def test_type_error_for_non_integer_input() -> None:
    with pytest.raises(TypeError, match="unsupported operand type"):
        get_coin_combination(None)
