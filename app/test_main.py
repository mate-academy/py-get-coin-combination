from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="0 cents test"
        ),
        pytest.param(
            3,
            [3, 0, 0, 0],
            id="3 pennies test"
        ),
        pytest.param(
            15,
            [0, 1, 1, 0],
            id="15 cents should convert to 1 dime and 1 nickel"
        ),
        pytest.param(
            28,
            [3, 0, 0, 1],
            id="28 cents should convert to 1 quarter and 3 pennies"
        ),
        pytest.param(
            42,
            [2, 1, 1, 1],
            id="42 cents convert to 1 quarter, 1 dime, 1 nickel and 2 cents"
        ),
        pytest.param(
            79,
            [4, 0, 0, 3],
            id="79 cents should convert to 3 quarters and 4 cents"
        ),
    ],
)
def test_get_coin_combination_custom(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
