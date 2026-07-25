from app.main import get_coin_combination

import pytest


def test_not_integer_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("coin")


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(0, [0, 0, 0, 0], id="test_zero_input"),
        pytest.param(1, [1, 0, 0, 0], id="test_one cent"),
        pytest.param(5, [0, 1, 0, 0], id="test_one cent"),
        pytest.param(10, [0, 0, 1, 0], id="test_one cent"),
        pytest.param(25, [0, 0, 0, 1], id="test_one cent"),
        pytest.param(174, [4, 0, 2, 6], id="test_one cent"),
    ]
)
def test_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
