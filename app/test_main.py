from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    # Test case for 1 cent
    assert get_coin_combination(1) == [1, 0, 0, 0]

    # Test case for 6 cents
    assert get_coin_combination(6) == [1, 1, 0, 0]

    # Test case for 17 cents
    assert get_coin_combination(17) == [2, 1, 1, 0]

    # Test case for 50 cents
    assert get_coin_combination(50) == [0, 0, 0, 2]

    # Additional test cases
    # Test case for 0 cents
    assert get_coin_combination(0) == [0, 0, 0, 0]

    # Test case for 99 cents
    assert get_coin_combination(99) == [4, 0, 2, 3]

    # Test case for 41 cents
    assert get_coin_combination(41) == [1, 1, 1, 1]
