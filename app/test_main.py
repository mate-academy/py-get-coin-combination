import pytest
from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(23) == [3, 0, 2, 0]
    assert get_coin_combination(18) == [3, 1, 1, 0]
    assert get_coin_combination(99) == [4, 0, 2, 3]


if __name__ == "__main__":
    pytest.main()
