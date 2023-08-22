from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [

        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Should correctly distribute the coins"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Should return smallest possible number"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="Should return zero if zero cents was given"
        )
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:

    assert get_coin_combination(cents) == expected
