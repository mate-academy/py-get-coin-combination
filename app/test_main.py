import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents gives no coins"),
        pytest.param(1, [1, 0, 0, 0], id="1 cent is 1 penny"),
        pytest.param(4, [4, 0, 0, 0], id="4 cents are 4 pennies"),
        pytest.param(5, [0, 1, 0, 0], id="5 cents is 1 nickel"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents is 1 penny and 1 nickel"),
        pytest.param(9, [4, 1, 0, 0], id="9 cents is 4 pennies and nickel"),
        pytest.param(10, [0, 0, 1, 0], id="10 cents is 1 dime"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents uses three coin types"),
        pytest.param(24, [4, 0, 2, 0], id="24 cents uses 2 dimes"),
        pytest.param(25, [0, 0, 0, 1], id="25 cents is 1 quarter"),
        pytest.param(41, [1, 1, 1, 1], id="41 cents uses every coin once"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents is 2 quarters"),
        pytest.param(99, [4, 0, 2, 3], id="99 cents uses max coins"),
        pytest.param(1000, [0, 0, 0, 40], id="large amount of cents"),
    ],
)
def test_returns_smallest_coin_combination(
        cents: int,
        expected: list[int],
) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", range(0, 200))
def test_coins_sum_up_to_given_amount(cents: int) -> None:
    pennies, nickels, dimes, quarters = main.get_coin_combination(cents)
    assert pennies + nickels * 5 + dimes * 10 + quarters * 25 == cents


def test_returns_list_of_four_elements() -> None:
    result = main.get_coin_combination(17)
    assert isinstance(result, list)
    assert len(result) == 4


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param("17", id="cents as string"),
        pytest.param(None, id="cents as None"),
        pytest.param([17], id="cents as list"),
    ],
)
def test_raises_type_error_for_invalid_types(cents: object) -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination(cents)
