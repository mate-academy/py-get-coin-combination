import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "test_input,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="list of zeroes if zero amount"),
        pytest.param(4, [4, 0, 0, 0], id="return pennies for correct amount"),
        pytest.param(6, [1, 1, 0, 0],
                     id="return pennies & nickels for correct amount"),
        pytest.param(
            18, [3, 1, 1, 0],
            id="return pennies, nickels & dimes for correct amount"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="return pennies, nickels, dimes & quarters for correct amount"
        ),
    ]
)
def test_return_correct_coin_combination(
        test_input: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(test_input) == expected
