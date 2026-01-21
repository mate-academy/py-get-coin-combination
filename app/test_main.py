import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (100, [0, 0, 0, 4]),
    ],
    ids=[
        "one_penny",
        "penny_and_nickel",
        "penny_nickel_dime",
        "two_quarters",
        "zero_cents",
        "four_quarters"
    ]
)
def test_get_coin_combination_examples(
    cents: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [-1, -10, -100],
    ids=["negative_one", "negative_ten", "negative_hundred"]
)
def test_get_coin_combination_negative_numbers(cents: int) -> None:
    assert get_coin_combination(cents) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents",
    ["10", [10], None],
    ids=["string_input", "list_input", "none_input"]
)
def test_get_coin_combination_raises_type_error(cents: any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
