import pytest
from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], "Failed on 1 cent"


def test_one_nickel_one_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0], "Failed on 6 cents"


def test_complex_combination() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0], "Failed on 17 cents"


def test_even_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2], "Failed on 50 cents"


def test_no_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0], "Failed on 0 cents"


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3], "Failed on 99 cents"


def test_non_integer_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("not_an_integer")
