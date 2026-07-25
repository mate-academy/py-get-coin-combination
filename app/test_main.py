from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(1, [1, 0, 0, 0], id="one cent"),
        pytest.param(41, [1, 1, 1, 1], id="all in one coin"),
        pytest.param(30, [0, 1, 0, 1], id="combination 30 cents"),
        pytest.param(99, [4, 0, 2, 3], id="combination 99 cents")
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
