from app.main import get_coin_combination


def test_coin_combination_for_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_coin_combination_for_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_coin_combination_for_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_coin_combination_for_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_coin_combination_for_0_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_coin_combination_for_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_coin_combination_for_same_amount_different_order() -> None:
    assert get_coin_combination(25) == [0, 0, 1, 0]


def test_coin_combination_for_large_amount_with_no_quarters() -> None:
    assert get_coin_combination(37) == [2, 0, 1, 1]
