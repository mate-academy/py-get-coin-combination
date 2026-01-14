import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="get_zero_value_except_zero_list"),
        pytest.param(4, [4, 0, 0, 0],
                     id="get_value_except_pennies"),
        pytest.param(9, [4, 1, 0, 0],
                     id="get_value_except_nickel_and_pennies"),
        pytest.param(10, [0, 0, 1, 0],
                     id="get_value_except_dime"),
        pytest.param(24, [4, 0, 2, 0],
                     id="get_value_except_dime_pennies"),
        pytest.param(25, [0, 0, 0, 1],
                     id="get_value_except_quarter"),
        pytest.param(67, [2, 1, 1, 2],
                     id="get_large_value_except_all_coins"),

    ]
)
def test_get_coin_combination(value: int, expected: list) -> None | str:
    assert (
        get_coin_combination(value) == expected
    ), f"{value} should be convert in {expected}"
