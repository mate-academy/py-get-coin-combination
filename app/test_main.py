import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="no money kids"),
        pytest.param(1, [1, 0, 0, 0], id="only penny test"),
        pytest.param(5, [0, 1, 0, 0], id="only nickel test"),
        pytest.param(10, [0, 0, 1, 0], id="only dimes test"),
        pytest.param(25, [0, 0, 0, 1], id="only quarter test"),
        pytest.param(69, [4, 1, 1, 2], id="different coins")
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
