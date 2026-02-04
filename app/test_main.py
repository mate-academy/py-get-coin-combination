import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, combination",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="penny should be first"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="convert 5 cents to 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="convert 10 cents to 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="convert 25 cents to 1 quarter"
        ),
    ]
)
def test_coin_combination(
        cents: int,
        combination: list
) -> None:
    assert get_coin_combination(cents) == combination
