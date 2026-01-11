from app.main import get_coin_combination


def test_check_if_sum_of_result_equal_cents() -> None:
    assert (
        get_coin_combination(1) == [1, 0, 0, 0]
    ), "1 cent should be 1 penny"
    assert (
        get_coin_combination(6) == [1, 1, 0, 0]
    ), "6 cents should be 1 penny and 1 nickel"
    assert (
        get_coin_combination(17) == [2, 1, 1, 0]
    ), "17 cents should be 2 pennies, 1 nickel, and 1 dime"
    assert (
        get_coin_combination(50) == [0, 0, 0, 2]
    ), "50 cents should be 2 quarters"
    assert (
        get_coin_combination(0) == [0, 0, 0, 0]
    ), "0 cents should be 0 coins"
    assert (
        get_coin_combination(99) == [4, 0, 2, 3]
    ), "99 cents should be 4 pennies, 2 dimes, and 3 quarters"
    assert (
        get_coin_combination(100) == [0, 0, 0, 4]
    ), "100 cents should be 4 quarters"
    assert (
        get_coin_combination(101) == [1, 0, 0, 4]
    ), "101 cents should be 1 penny and 4 quarters"
    assert (
        get_coin_combination(123) == [3, 0, 2, 4]
    ), "123 cents should be 3 pennies, 2 dimes, and 4 quarters"

    try:
        get_coin_combination(-1)
    except ValueError:
        print("Expected ValueError for negative input")

    try:
        get_coin_combination("100")
    except TypeError:
        print("Expected TypeError for string input")

    try:
        get_coin_combination(10.5)
    except TypeError:
        print("Expected TypeError for float input")
