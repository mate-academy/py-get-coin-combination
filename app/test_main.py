from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="Return only pennie"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="Return only nickel"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="Return only dime"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="Return only quarter"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="Return coins combinations"
        )

    ]
)
def test_logic_of_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
