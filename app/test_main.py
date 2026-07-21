import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="Should return 1 penny if coin is 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Should return 1 penny + 1 nickel if cents is 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Should return 2 pennies + 1 nickel + 1 dime if cents is 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Should return 2 quarters if cents is 50"
        )
    ]
)
def test_fucntion_working_correctly(
    cents: int,
    result: list
) -> None:
    assert get_coin_combination(cents) == result
