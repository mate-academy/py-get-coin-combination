from app.main import get_coin_combination


def test_should_return_zero_coins_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_pennies_for_small_amounts() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_combination_with_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_combination_with_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_combination_with_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(92) == [2, 1, 1, 3]


def test_should_handle_large_amounts() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
