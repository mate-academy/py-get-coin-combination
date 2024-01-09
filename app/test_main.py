import pytest
from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]

    # Additional test cases
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(11) == [1, 0, 1, 0]
    assert get_coin_combination(99) == [4, 0, 2, 3]

    # Edge case with a large amount
    assert get_coin_combination(999) == [4, 0, 2, 39]


if __name__ == "__main__":
    pytest.main()
