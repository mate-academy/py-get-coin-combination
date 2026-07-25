import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 penny",
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="1 penny 1 nickel",
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="2 pennies 1 nickel 1 dime",
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="2 quarters",
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="0 cents",
        ),
        pytest.param(
            1234,
            [4, 1, 0, 49],
            id="large value",
        ),
        pytest.param(
            75,
            [0, 0, 0, 3],
            id="only quarters",
        ),
        pytest.param(
            80,
            [0, 1, 0, 3],
            id="only dimes",
        ),
        pytest.param(
            15,
            [0, 1, 1, 0],
            id="only nickels",
        ),
        pytest.param(
            7,
            [2, 1, 0, 0],
            id="only pennies",
        ),
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
