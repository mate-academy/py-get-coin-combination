from app.main import get_coin_combination


def test_only_pennies_in_result() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test_only_nickels_in_result() -> None:
    result = get_coin_combination(5)
    assert result == [0, 1, 0, 0]


def test_only_dimes_in_result() -> None:
    result = get_coin_combination(10)
    assert result == [0, 0, 1, 0]


def test_only_quarters_in_result() -> None:
    result = get_coin_combination(25)
    assert result == [0, 0, 0, 1]


def test_coins_of_different_types() -> None:
    result = get_coin_combination(42)
    assert result == [2, 1, 1, 1]
