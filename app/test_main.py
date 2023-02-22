import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(0, [], id="zero cents"),
        pytest.param(5, [0, 1, 0, 0], id="1 coin type"),
        pytest.param(41, [1, 1, 1, 1], id="all coin types"),
        pytest.param(55, [0, 1, 0, 2], id="two coin types")
    ]
)
def test_correct_coin_combination(cents: int, result: list) -> None:
    assert (get_coin_combination(cents) == result,
            f"combination for {cents} cents should be {result}")
