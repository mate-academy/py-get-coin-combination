from app.main import get_coin_combination


def test_with_only_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0], \
        "Should return correct number of pennies"


def test_with_pennies_and_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0], \
        "Should use pennies and nickels correctly"


def test_with_pennies_nickels_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0], \
        "Should use pennies, nickels, and dimes correctly"


def test_with_all_coin_types() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2], \
        "Should use all types of coins correctly"


def test_with_no_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0], \
        "Should return all zeros for 0 cents"
