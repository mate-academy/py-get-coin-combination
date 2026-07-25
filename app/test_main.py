import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 cent to coin equal"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents to coin equal"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents to coin equal"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents to coin equal"),
        pytest.param(10, [0, 0, 1, 0], id="10 cents to coin equal"),
        pytest.param(25, [0, 0, 0, 1], id="25 cents to coin equal"),
        pytest.param(5, [0, 1, 0, 0], id="5 cents to coin equal"),
        pytest.param(117, [2, 1, 1, 4], id="117 cents to coin equal"),
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
