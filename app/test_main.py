from app.main import get_coin_combination


def test_get_coin_combination_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_big_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
