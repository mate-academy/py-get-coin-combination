import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin,coin_combination",
    [
        pytest.param(
            67, [2, 1, 1, 2],
            id=" 67 should be 2penny, 1nickel, 1dime, 1quarter"
        ),
        pytest.param(
            -4, [1, 0, 2, -1],
            id="-4 converted to 0"
        ),
        pytest.param(
            112, [2, 0, 1, 4],
            id="112 should be 2penny, 1dime, 4 quarter"
        ),
        pytest.param(
            75, [0, 0, 0, 3],
            id="75 should be 3 quarter"
        ),
        pytest.param(
            14, [4, 0, 1, 0],
            id="14 should be 4 penny and 1 dime"
        ),
    ]
)
def test_get_coin_combination(coin: int, coin_combination: list) -> None:
    assert (get_coin_combination(coin) == coin_combination)
