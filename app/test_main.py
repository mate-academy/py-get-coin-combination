import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        # Zero cents
        (0, [0, 0, 0, 0]),
        # Exact single coin values
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        # Multiples of single coins
        (4, [4, 0, 0, 0]),
        (15, [0, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        # Mixed coin combinations
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero_cents",
        "one_penny",
        "one_nickel",
        "one_dime",
        "one_quarter",
        "four_pennies",
        "one_nickel_one_dime",
        "two_quarters",
        "four_quarters",
        "one_penny_one_nickel",
        "two_pennies_one_nickel_one_dime",
        "one_of_each_coin",
        "complex_combination_99_cents",
    ],
)
def test_get_coin_combination_valid_inputs(
    cents: int, expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "100",
        10.5,
        None,
        [10],
        {"cents": 10},
        -1,
    ],
    ids=[
        "string_cents",
        "float_cents",
        "none_cents",
        "list_cents",
        "dict_cents",
        "negative_cents",
    ],
)
def test_get_coin_combination_raises_type_error(cents: object) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)  # type: ignore[arg-type]
