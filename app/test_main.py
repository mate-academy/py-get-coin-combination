import pytest
from app.main import get_coin_combination


def test_should_return_list():
    assert isinstance(get_coin_combination(1), list)

def test_should_return_correct_length():
    assert len(get_coin_combination(1)) == 4

@pytest.mark.parametrize("cents, expected", [
    pytest.param(0,  [0, 0, 0, 0], id="0_cents"),
    pytest.param(1,  [1, 0, 0, 0], id="1_penny"),
    pytest.param(2,  [2, 0, 0, 0], id="2_pennies"),
    pytest.param(4,  [4, 0, 0, 0], id="4_pennies"),
    pytest.param(5,  [0, 1, 0, 0], id="1_nickel"),
    pytest.param(6,  [1, 1, 0, 0], id="1_penny_1_nickel"),
    pytest.param(10, [0, 0, 1, 0], id="1_dime"),
    pytest.param(17, [2, 1, 1, 0], id="2_pennies_1_nickel_1_dime"),
    pytest.param(20, [0, 0, 2, 0], id="2_dimes"),
    pytest.param(25, [0, 0, 0, 1], id="1_quarter"),
    pytest.param(30, [0, 1, 0, 1], id="1_nickel_1_quarter"),
    pytest.param(50, [0, 0, 0, 2], id="2_quarters"),
    pytest.param(75, [0, 0, 0, 3], id="3_quarters"),
    pytest.param(99, [4, 0, 2, 3], id="99_cents_mixed"),
    pytest.param(100, [0, 0, 0, 4], id="1_dollar_4_quarters"),
])
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected


def test_returns_only_integers():
    result = get_coin_combination(87)
    assert all(isinstance(x, int) for x in result)


def test_all_values_non_negative():
    result = get_coin_combination(150)
    assert all(x >= 0 for x in result)
