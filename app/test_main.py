from app.main import get_coin_combination


def test_get_coin_combination_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_mixed_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_edge_case_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_exact_dollar() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
