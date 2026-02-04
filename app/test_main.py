import pytest
from app.main import get_coin_combination


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_exact_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_nickel_plus_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_before_dime() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_exact_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_dime_plus_penny() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_example_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_before_quarter() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_exact_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_quarter_plus_penny() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]


def test_example_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_mixed_large_amount() -> None:
    # 99 = 3*25 (75) + 2*10 (20) + 0*5 + 4*1
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_wrong_type_raises() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("10")
