import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(50, [0, 0, 0, 2], id="test_quarters"),
        pytest.param(20, [0, 0, 2, 0], id="test_dimes"),
        pytest.param(5, [0, 1, 0, 0], id="test_nickels"),
        pytest.param(4, [4, 0, 0, 0], id="test_pennies"),
        pytest.param(0, [0, 0, 0, 0], id="test_input_equals_0"),
        pytest.param(1.15, [1.0, 0, 0, 0], id="test_float_input")
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_if_function_raises_typeerror() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("")
