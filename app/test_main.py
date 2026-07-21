from app.main import get_coin_combination


def test_exact_coin_values() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]  # 1 nickel
    assert get_coin_combination(10) == [0, 0, 1, 0]  # 1 dime
    assert get_coin_combination(25) == [0, 0, 0, 1]  # 1 quarter


def test_combinations_of_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(16) == [1, 1, 1, 0]
    assert get_coin_combination(40) == [0, 1, 1, 1]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_number_of_cents() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_random_values() -> None:
    # Test a series of random values
    assert get_coin_combination(7) == [2, 1, 0, 0]
    assert get_coin_combination(27) == [2, 0, 0, 1]
