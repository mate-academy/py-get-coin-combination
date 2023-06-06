from typing import Any

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="Function should return 1 cent!"),
        pytest.param(
            6, [1, 1, 0, 0],
            id="The function should return 1 nickels and 1 penny!"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="It should be: [2, 1, 1, 0] == 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="It should be:  [0, 0, 0, 2] == 2 quarters"
        )
    ]
)
def test_function_get_coin_result(cents: int, result: list) -> None:

    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param("123", id="Function should return TypeError!"),
        pytest.param({123}, id="Function should return TypeError!")
    ]
)
def test_function_get_coin_true_error(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
