import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="return no coins for zero"),
        pytest.param(1, [1, 0, 0 , 0], id="one penny"),
        pytest.param(6, [1, 1, 0, 0], id="one penny and on nickel"),
        pytest.param(17, [2, 1, 1, 0], id="two pennies, one nickel, one dime"),
        pytest.param(25, [0, 0, 0, 1], id="prefer quarter over smaller coins"),
        pytest.param(50, [0, 0, 0, 2], id="two quarters"),
        pytest.param(41, [1, 1, 1, 1], id="all coin types"),
        pytest.param(16, [1, 1, 1, 0], id="penny-nickel-dime"),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
#
# def test_should_return_no_coins_for_zero():
#     assert get_coin_combination(0) == [0, 0, 0, 0]
#
# def test_should_one_more_penny():
#     assert get_coin_combination(1) == [1, 0, 0, 0]
#
# def test_should_one_penny_and_one_nickel():
#     assert get_coin_combination(6) == [1, 1, 0, 0]
#
# def test_should_two_pennies_one_nickel_one_dime():
#     assert get_coin_combination(17) == [2, 1, 1, 0]
#
# def test_should_prefer_quarter_over_smaller_coins():
#     assert get_coin_combination(25) == [0, 0, 0, 1]
#
# def test_should_two_quarters():
#     assert get_coin_combination(50) == [0, 0 ,0 , 2]
