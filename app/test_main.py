from app.main import get_coin_combination
import pytest


# write your tests here
@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="test only cents"),
        pytest.param(6, [1, 1, 0, 0], id="test cents and nickels"),
        pytest.param(17, [2, 1, 1, 0], id="test cents, nickels and dimes"),
        pytest.param(67, [2, 1, 1, 2],
                     id="test cents, nickels, dimes and quarters"),
        pytest.param(314159265359, [4, 1, 0, 12566370614],
                     id="test cents, nickels, dimes and quarters"),
    ]
)
def test_all_possible_coin_denominations_are_used(cents: int,
                                                  result: list) -> None:
    assert (result == get_coin_combination(cents))
