from app.main import get_coin_combination


def test_coin_combination() -> None:
    """
    Test the get_coin_combination function.
    """
    # 3 quarters, 2 dimes, 0 nickels, 4 pennies = 99 cents
    assert get_coin_combination(99) == [4, 0, 2, 3]
