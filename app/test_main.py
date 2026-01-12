import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="penny test "),
        pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel test"),
        pytest.param(17, [2, 1, 1, 0], id="2pennies + nickel + dime test"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters test"),
    ],

)
def test_get_coin_combination(cents: int | str,
                              result: int | str,
                              ) -> None:
    assert get_coin_combination(cents) == result
