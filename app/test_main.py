import pytest
from app.main import get_coin_combination


def test_single_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0],\
        f"Expected [1, 0, 0, 0], but got {get_coin_combination(1)}"
    assert get_coin_combination(5) == [0, 1, 0, 0],\
        f"Expected [0, 1, 0, 0], but got {get_coin_combination(5)}"
    assert get_coin_combination(10) == [0, 0, 1, 0],\
        f"Expected [0, 0, 1, 0], but got {get_coin_combination(10)}"
    assert get_coin_combination(25) == [0, 0, 0, 1],\
        f"Expected [0, 0, 0, 1], but got {get_coin_combination(25)}"


def test_combination_of_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0],\
        f"Expected [1, 1, 0, 0], but got {get_coin_combination(6)}"
    assert get_coin_combination(17) == [2, 1, 1, 0],\
        f"Expected [2, 1, 1, 0], but got {get_coin_combination(17)}"
    assert get_coin_combination(41) == [1, 1, 1, 1],\
        f"Expected [1, 1, 1, 1], but got {get_coin_combination(41)}"
    assert get_coin_combination(99) == [4, 0, 2, 3],\
        f"Expected [4, 0, 2, 3], but got {get_coin_combination(99)}"


def test_large_amount() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4],\
        f"Expected [0, 0, 0, 4], but got {get_coin_combination(100)}"
    assert get_coin_combination(123) == [3, 0, 2, 4],\
        f"Expected [3, 0, 2, 4], but got {get_coin_combination(123)}"


def test_zero_amount() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0],\
        f"Expected [0, 0, 0, 0], but got {get_coin_combination(0)}"


if __name__ == "__main__":
    pytest.main()
