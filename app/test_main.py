import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (43, [3, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero_cents",
        "one_penny",
        "four_pennies",
        "exactly_one_nickel",
        "nickel_and_pennies",
        "exactly_one_dime",
        "before_quarter_boundary",
        "exactly_one_quarter",
        "example_6_cents",
        "example_17_cents",
        "example_50_cents",
        "complex_combination_43",
        "large_number_99"
    ]
)
def test_get_coin_combination_standard_cases(cents: int, expected: list[int])\
        -> None:
    result = get_coin_combination(cents)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 4


def test_should_return_all_zeros_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_mathematical_total_value_matches() -> None:
    cents = 68
    result = get_coin_combination(cents)
    total_calculated = (result[0] * 1
                        + result[1] * 5 + result[2] * 10 + result[3] * 25)
    assert total_calculated == cents
