from app.main import get_coin_combination


def test_get_coin_combination_one_penny() -> None:
    """Test for 1 cent: should return 1 penny."""
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_six_cents() -> None:
    """Test for 6 cents: should return 1 penny and 1 nickel."""
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_seventeen_cents() -> None:
    """Test for 17 cents: should return 2 pennies, 1 nickel, and 1 dime."""
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_fifty_cents() -> None:
    """Test for 50 cents: should return 2 quarters."""
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_zero_cents() -> None:
    """Test for 0 cents: should return no coins."""
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_twenty_five_cents() -> None:
    """Test for 25 cents: should return 1 quarter."""
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_ten_cents() -> None:
    """Test for 10 cents: should return 1 dime."""
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_five_cents() -> None:
    """Test for 5 cents: should return 1 nickel."""
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_ninety_nine_cents() -> None:
    """Test for 99 cents: should return 3 quarters,
    2 dimes, 0 nickels, and 4 pennies."""
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_large_amount() -> None:
    """Test for a large amount, e.g., 1000 cents (10 dollars)."""
    assert get_coin_combination(1000) == [0, 0, 0, 40]


def test_get_coin_combination_mixed_coins() -> None:
    """Test for 36 cents: should return 1 penny, 0 nickels, and 3 dimes."""
    assert get_coin_combination(36) == [1, 0, 1, 1]


def test_get_coin_combination_mixed_coins_with_quarters() -> None:
    """Test for 67 cents: should return 2 pennies,
    1 nickel, 1 dime, and 2 quarters."""
    assert get_coin_combination(67) == [2, 1, 1, 2]
