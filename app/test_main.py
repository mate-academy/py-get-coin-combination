from app.main import get_coin_combination


def test_combination_of_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1], \
        "Should return combination of all coin types"
    assert get_coin_combination(6) == [1, 1, 0, 0], \
        "Should return pennies and nickels"
    assert get_coin_combination(30) == [0, 0, 3, 0], \
        "Should return only dimes"


def test_return_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], \
        "Should return one penny"
    assert get_coin_combination(5) == [0, 1, 0, 0], \
        "Should return one nickel"
    assert get_coin_combination(10) == [0, 0, 1, 0], \
        "Should return one dime"


def test_return_only_one_type() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0], \
        "Should return only nickels"
    assert get_coin_combination(10) == [0, 0, 1, 0], \
        "Should return only dimes"
    assert get_coin_combination(25) == [0, 0, 0, 1], \
        "Should return only quarters"
