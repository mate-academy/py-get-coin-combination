from app.main import get_coin_combination


def test_returns_zero_coins_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_returns_only_pennies_for_small_amount() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_returns_mixed_coins_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_returns_mixed_coins_for_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_returns_only_quarters_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_returns_combination_with_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
