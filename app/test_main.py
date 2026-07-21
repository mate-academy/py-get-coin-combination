from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="one cent"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents"),
        pytest.param(25, [0, 0, 0, 1], id="fifty cents"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents"),
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    )
