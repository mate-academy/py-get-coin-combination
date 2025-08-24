from app.main import get_coin_combination


def test_coin_combination() -> None:
    """
    Test the get_coin_combination function.
    """
    # 3 quarters, 2 dimes, 0 nickels, 4 pennies
    assert get_coin_combination(99) == [3, 2, 0, 4]

    assert get_coin_combination(0) == [0, 0, 0, 0]

    # 1 quarter, 1 dime, 1 nickel, 1 penny
    assert get_coin_combination(41) == [1, 1, 1, 1]
