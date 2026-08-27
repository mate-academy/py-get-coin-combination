import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="output with zero value"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="output is 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="output is 1 penny and 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="output is 2 pennies 1 nickel and 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="output is 2 quarters"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="max pennies before nickel (4 cents)"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="max pennies and nickel before dime (9 cents)"
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id="max pennies and dimes before quarter (24 cents)"
        ),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
