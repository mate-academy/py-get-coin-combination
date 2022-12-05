from app.main import get_coin_combination


def test_when_cents_amount_only_use_penny_coins() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_when_cents_amount_only_use_penny_and_nickel_coins() -> None:
    assert get_coin_combination(8) == [3, 1, 0, 0]


def test_when_cents_amount_use_everything_except_quarter_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_when_cents_amount_use_all_possible_coins() -> None:
    assert get_coin_combination(68) == [3, 1, 1, 2]
