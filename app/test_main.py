from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, convert_list", [
        pytest.param(1, [1, 0, 0, 0],
                     id="1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="2 pennies + 1 nickel +1 dime"),
        pytest.param(50, [0, 0, 0, 2],
                     id="2 quarters")
    ]
)
def test_get_coin_combination(
        cents: int,
        convert_list: list
) -> None:
    assert get_coin_combination(cents) == convert_list
