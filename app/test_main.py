from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return all zeros for zero cent"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return one penny for one cent"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1 penny, 1 nickel for 6 cents"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 2 pennies, 1 nickel, 1 dime for 17 cents"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 2 quarters for 50 cents"
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id="should return 4 pennies, 2 dimes for 24 cents"
        ),
        pytest.param(
            257,
            [2, 1, 0, 10],
            id="should return 2 pennies, 1 nickel, 10 quarters for 257 cents"
        ),
        pytest.param(
            49,
            [4, 0, 2, 1],
            id="should return 4 pennies, 2 dimes, 1 quarter for 49 cents"
        )
    ]
)
def test_should_return_correct_values(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
