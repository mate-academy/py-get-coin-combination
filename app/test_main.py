import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("coins,coin_combo", [
    pytest.param(1, [1, 0, 0, 0]),
    pytest.param(6, [1, 1, 0, 0]),
    pytest.param(17, [2, 1, 1, 0]),
    pytest.param(50, [0, 0, 0, 2])
], ids=["1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters"]
)
def test_coin_combination(coins: int, coin_combo: list) -> None:
    assert get_coin_combination(coins) == coin_combo


def test_invalid_input_type_raises_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("a")
