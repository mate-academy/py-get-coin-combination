from app.main import get_coin_combination


def test_cents_less_than_5() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_cents_less_than_10() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_cents_less_than_25() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_cents_more_than_25() -> None:
    assert get_coin_combination(104) == [4, 0, 0, 4]
