import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero_cents_returns_no_coins"),
        pytest.param(1, [1, 0, 0, 0], id="one_penny"),
        pytest.param(5, [0, 1, 0, 0], id="one_nickel"),
        pytest.param(6, [1, 1, 0, 0], id="penny_and_nickel"),
        pytest.param(10, [0, 0, 1, 0], id="one_dime"),
        pytest.param(17, [2, 1, 1, 0], id="two_pennies_nickel_dime"),
        pytest.param(25, [0, 0, 0, 1], id="one_quarter"),
        pytest.param(50, [0, 0, 0, 2], id="two_quarters"),
        pytest.param(99, [4, 0, 2, 3], id="ninety_nine_cents"),
        pytest.param(100, [0, 0, 0, 4], id="one_dollar_four_quarters"),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


def test_get_coin_combination_returns_list() -> None:
    assert isinstance(main.get_coin_combination(17), list)


def test_get_coin_combination_length_is_four() -> None:
    assert len(main.get_coin_combination(17)) == 4
