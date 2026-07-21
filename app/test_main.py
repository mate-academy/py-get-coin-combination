from app.main import get_coin_combination


def test_returns_zero_with_zero_argument() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_returns_penny_correctly() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_returns_nickels_without_pennies_correctly() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_returns_nickels_and_pennies_correctly() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_returns_dimes_without_nickels_and_pennies_correctly() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_returns_dimes_with_nickels_and_pennies_correctly() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_returns_quarters_only_correctly() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_returns_one_of_all_coins_correctly() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
