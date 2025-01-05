import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(1, [1, 0, 0, 0], id="one pennie"),
        pytest.param(5, [0, 1, 0, 0], id="one nickel"),
        pytest.param(10, [0, 0, 1, 0], id="one dime"),
        pytest.param(25, [0, 0, 0, 1], id="one quarter"),
        pytest.param(1973, [3, 0, 2, 78], id="many cents"),
        pytest.param(-1, [4, 0, 2, -1], id="argument is non-negative integer")
    ]
)
def test_calculate_coin(
        cents: int,
        coins: list[int]
) -> None:
    assert get_coin_combination(cents) == coins


@pytest.mark.parametrize(
    "cents,error",
    [
        pytest.param("1", TypeError, id="argument is integer"),
    ]
)
def test_value_type(
        cents: int,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_coin_combination(cents)
