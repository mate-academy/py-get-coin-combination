from app.main import get_coin_combination


def test_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_55_cent() -> None:
    assert get_coin_combination(55) == [0, 1, 0, 2]
