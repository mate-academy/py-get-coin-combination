import pytest
from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    # Test cases
    assert get_coin_combination(0) == [0, 0, 0, 0]  # 0 cents
    assert get_coin_combination(1) == [1, 0, 0, 0]  # 1 penny
    assert get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]  # 2 quarters
    assert get_coin_combination(99) == [4, 0, 2, 3]

    # Edge case: negative value
    with pytest.raises(ValueError):
        get_coin_combination(-1)

    # Edge case: floating-point value
    with pytest.raises(ValueError):
        get_coin_combination(3.14)

    # Edge case: invalid input type
    with pytest.raises(TypeError):
        get_coin_combination("string")
