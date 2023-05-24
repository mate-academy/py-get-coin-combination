import pytest
from app.main import get_coin_combination


def test_value_should_be_positive() -> None:
    cents = -55
    assert (
        cents >= 0
    ), "Value should be positive"


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),

    ],
    ids=[
        "Should return all values is 0 if cents is 0",
        "Should return 1 pennie if cents is 1",
        "Should return 4 pennie if cents is 4",
        "Should return 1 nickels if cents is 5",
        "Should return 1 nickels and 1 pennie if cents is 6",
        "Should return 1 nickels and 4 pennie if cents is 9",
        "Should return 1 dimes if cents is 10",
        "Should return 1 dimes and 1 pennie if cents is 11",
        "Should return 2 dimes and 4 pennie if cents is 24",
        "Should return 1 quarters if cents is 25",
        "Should return 1 quarters and 1 pennie if cents is 26",
    ]
)
def test_function_should_calculate_correctly(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), "Function should calculate correctly"
