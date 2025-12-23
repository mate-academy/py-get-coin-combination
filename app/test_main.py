from app.main import get_coin_combination


def test_combination_of_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_zero_cents_should_return_all_zeros() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_combination_with_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_combination_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_only_pennies() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_large_amount_combination() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_should_use_minimal_number_of_coins() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]
