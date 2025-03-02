from app.main import get_coin_combination


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_single_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_single_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_single_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
    assert get_coin_combination(17) == [2, 1, 1, 0]  # 2 pennies + 1 nickel
    # + 1 dime
    assert get_coin_combination(50) == [0, 0, 0, 2]  # 2 quarters
    assert get_coin_combination(99) == [4, 0, 2, 3]  # 4 pennies
    # + 2 dimes + 3 quarters


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]  # 4 quarters
    assert get_coin_combination(123) == [3, 0, 2, 4]  # 3 pennies
    # + 2 dimes + 4 quarters


def test_boundary_conditions() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]
    assert get_coin_combination(49) == [4, 0, 2, 1]
    assert get_coin_combination(74) == [4, 0, 2, 2]
    assert get_coin_combination(99) == [4, 0, 2, 3]
