from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_single_coins() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]  # 1 nickel
    assert get_coin_combination(10) == [0, 0, 1, 0]  # 1 dime
    assert get_coin_combination(25) == [0, 0, 0, 1]  # 1 quarter


def test_mixed_combinations() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
    assert get_coin_combination(17) == [
        2, 1, 1, 0
    ]  # 2 pennies + 1 nickel + 1 dime
    assert get_coin_combination(50) == [0, 0, 0, 2]  # 2 quarters


# Complex combinations
def test_complex_amount() -> None:
    # 99 cents = 3 quarters (75) + 2 dimes (20) + 4 pennies (4)
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_large_amount() -> None:
    # 126 cents = 5 quarters (125) + 1 penny (1)
    assert get_coin_combination(126) == [1, 0, 0, 5]
