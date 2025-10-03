from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel_and_one_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dime_nickel_and_pennies() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_exactly_one_of_each_coin() -> None:
    # 1 quarter (25) + 1 dime (10) + 1 nickel (5) + 1 penny (1) = 41
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_large_amount() -> None:
    # 99 cents = 3 quarters (75) + 2 dimes (20) + 0 nickels + 4 pennies
    assert get_coin_combination(99) == [4, 0, 2, 3]
