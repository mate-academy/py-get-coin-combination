from app.main import get_coin_combination


def test_cents_amount_is_above_24() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_cents_amount_is_between_10_24() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_cents_amount_is_between_5_9() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_cents_amount_is_below_5() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
