import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expect_coins",
    [
        pytest.param(0, [0, 0, 0, 0], id="test for cents penny"),
        pytest.param(1, [1, 0, 0, 0], id="test for 1 cent"),
        pytest.param(6, [1, 1, 0, 0], id="test for 6 cents"),
        pytest.param(17, [2, 1, 1, 0], id="test for 27 cents"),
        pytest.param(41, [1, 1, 1, 1], id="test for 41 penny"),
        pytest.param(1111, [1, 0, 1, 44], id="test for 1111 penny")
    ]
)
def test_coin_combination(
        cents: int,
        expect_coins: list[int]
) -> None:
    assert get_coin_combination(cents) == expect_coins
