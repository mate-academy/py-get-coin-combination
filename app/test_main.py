import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_output",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return all 0 when cents=0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny when cents=1"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="should return 4 pennies and 1 nickel when cents=9"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="should return 1 dime when cents=10"
        ),
        pytest.param(
            45,
            [0, 0, 2, 1],
            id="should return 1 quarter and 2 dimes when cents=45"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return 1 quarter, 1 dime, 1 nickel, "
               "and 1 penny when cents=41"
        )
    ]
)
def test_coin_combination(cents: int, expected_output: list[int]):
    assert get_coin_combination(cents) == expected_output
