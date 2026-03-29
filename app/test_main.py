import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, expectation",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
    ]
)
def test_get_coin_combination(cent: int, expectation: list) -> None:
    assert get_coin_combination(cent) == expectation


@pytest.mark.parametrize(
    "cent",
    [
        pytest.param([], id="list"),
        pytest.param({}, id="dict"),
    ]
)
def test_error_in_func(cent: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cent)
