import pytest

from app.main import get_coin_combination


def test_func_return_list():
    assert isinstance(get_coin_combination(123), list)


def test_func_return_right_len():
    assert len(get_coin_combination(123)) == 4


def test_fun_can_convert_all_values():
    assert 0 not in get_coin_combination(41)


def test_fun_can_convert_all_values():
    assert get_coin_combination(40)[1] == 1
    assert get_coin_combination(40)[2] == 1
    assert get_coin_combination(40)[3] == 1


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=["coins -> penny",
         "coins -> penny + nickel",
         "coins -> 2 pennies + nickel + dime",
         "coins -> quarters"]
)
def test_func_should_return_expected_results(cents, result):
    assert (
            get_coin_combination(cents) == result
    )
