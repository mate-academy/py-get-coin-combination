import pytest

from app.main import get_coin_combination


def test_func_return_list():
    assert isinstance(get_coin_combination(123), list)


def test_func_return_right_len():
    assert len(get_coin_combination(123)) == 4


def test_fun_can_convert_all_values():
    assert 0 not in get_coin_combination(41)


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=["penni",
         "nickel convert",
         "dime convert",
         "quarter convert"]
)
def test_big_parametrize_daddy(cents, result):
    assert (
            get_coin_combination(cents) == result
    )
