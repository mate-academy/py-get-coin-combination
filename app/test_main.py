import pytest

from app.main import get_coin_combination


def test_should_return_list_of_four_elements() -> None:
    assert len(get_coin_combination(17)) == 4, (
        "Result should contain exactly four elements: "
        "[pennies, nickels, dimes, quarters]"
    )


def test_sum_of_coins_should_be_equal_to_cents() -> None:
    pennies, nickels, dimes, quarters = get_coin_combination(99)
    total = pennies + nickels * 5 + dimes * 10 + quarters * 25
    assert total == 99, (
        "Total value of all coins should be equal to 'cents'"
    )


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero cents give no coins",
        "one cent gives one penny",
        "four cents: max pennies before nickel",
        "five cents give one nickel",
        "six cents give penny and nickel",
        "nine cents: max amount before dime",
        "ten cents give one dime",
        "seventeen cents: penny nickel dime",
        "twenty four cents: max amount before quarter",
        "twenty five cents give one quarter",
        "fifty cents give two quarters",
        "ninety nine cents combine all coin types",
    ],
)
def test_get_coin_combination_boundary_values(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected, (
        f"get_coin_combination({cents}) "
        f"should return {expected}"
    )


@pytest.mark.parametrize(
    "cents",
    ["17", None],
    ids=[
        "cents as string",
        "cents as None",
    ],
)
def test_incorrect_types_should_raise_type_error(
    cents: str | None,
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
