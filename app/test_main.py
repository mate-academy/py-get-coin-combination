import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    ("cents", "expected_result"),
    [
        pytest.param(
            100, [0, 0, 0, 4],
            id="should return only quarters if cents divisible by 25"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should return one dime if cents are 10"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="should return one nickel if cents are 5"
        ),
        pytest.param(
            4, [4, 0, 0, 0],
            id="should return only pennies if cents up to 5"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="should return one of each coin if cents are 41"
        )
    ]
)
def test_function(cents: int, expected_result: list[int]) -> None:
    assert get_coin_combination(cents) == expected_result
