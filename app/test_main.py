from app.main import get_coin_combination


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_all_types() -> None:
    # 2 pennies, 1 nickel, 1 dime = 2 + 5 + 10 = 17
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_mixed_large() -> None:
    # 99 cents = 3 quarters (75), 2 dimes (20), 4 pennies (4)
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_exact_one_each() -> None:
    # 1 penny + 1 nickel + 1 dime + 1 quarter = 41 cents
    assert get_coin_combination(41) == [1, 1, 1, 1]
