import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(0, [0, 0, 0, 0], id="receive only zeros"),
        pytest.param(1, [1, 0, 0, 0], id="receive only penny"),
        pytest.param(6, [1, 1, 0, 0], id="receive penny and nickel"),
        pytest.param(18, [3, 1, 1, 0], id="receive penny, nickel and dime"),
        pytest.param(50, [0, 0, 0, 2], id="receive quarters"),
        pytest.param(256, [1, 1, 0, 10], id="work with big number")
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

def test_incorrect_value() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("2")
