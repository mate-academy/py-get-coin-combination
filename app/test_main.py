import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,expected",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="Check transferring 1 cent"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="Check transferring 6 cents"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="Check transferring 17 cents"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="Check transferring 50 cents"
        )
    ]
)
def test_get_coin_combination(coins: int, expected: list) -> None:
    assert get_coin_combination(coins) == expected
