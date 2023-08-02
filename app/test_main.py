from app.main import get_coin_combination


def test_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
