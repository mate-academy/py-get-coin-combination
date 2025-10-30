import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, expected",
    [
        pytest.param(
            1, [1, 0, 0, 0], id="1 cent is 1 penny"
        ),
        pytest.param(
            6, [1, 1, 0, 0], id="6 cents is 1 penny and 1 nickel"
        ),
        pytest.param(
            17, [2, 1, 1, 0], id="17 cent is 2 pennies and 1 nickel and 1 dime"
        ),
        pytest.param(
            50, [0, 0, 0, 2], id="50 cents is rapper"
        )
    ]
)
def test_get_coin_combination(coin: int, expected: list) -> None:
    assert get_coin_combination(coin) == expected
