from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_15_cents_minimal() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_mixed_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_example_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_example_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_example_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_not_only_pennies() -> None:
    result = get_coin_combination(30)
    assert result != [30, 0, 0, 0]


def test_uses_different_coin_types() -> None:
    result = get_coin_combination(41)
    non_zero_coins = sum(1 for coin in result if coin > 0)
    assert non_zero_coins
