import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        pytest.param(0, [0, 0, 0, 0],
                     id="Test with 0"),
        pytest.param(1, [1, 0, 0, 0],
                     id="Test with 1"),
        pytest.param(6, [1, 1, 0, 0],
                     id="Test with 6"),
        pytest.param(18, [3, 1, 1, 0],
                     id="Test with 18"),
        pytest.param(51, [1, 0, 0, 2],
                     id="Test with 51")
    ]
)
def test_the_results(coins: int, result: int) -> None:
    assert (
        get_coin_combination(coins) == result
    )
