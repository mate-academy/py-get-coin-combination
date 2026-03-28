import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected", [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="Should return  penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Should return penny and nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Should return pennies, nickel and dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Should return quarters"
        )
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
