import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="Return [0, 0, 0, 0] coins parameter is zero"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="Return [0, 0, 0, 0] coins parameter is 1"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="Return [0, 0, 0, 0] coins parameter is 1"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="Return [0, 0, 0, 0] coins parameter is 1"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="Return [0, 0, 0, 0] coins parameter is 1"
        )
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
