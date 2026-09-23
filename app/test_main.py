import pytest

from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_four_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_two_pennies_one_nickel_one_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_dime_and_nickel() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_two_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_quarter_dime_nickel_penny() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_ninety_nine_cents_breakdown() -> None:
    # 99 = 3*25 + 2*10 + 0*5 + 4*1 = 75+20+0+4
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_hundred_cents() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


@pytest.mark.parametrize("cents", [1, 2, 3, 4])
def test_small_penny_only_amounts(cents: int) -> None:
    assert get_coin_combination(cents) == [cents, 0, 0, 0]
