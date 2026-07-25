from app.main import get_coin_combination


def test_get_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_8_cents() -> None:
    assert get_coin_combination(8) == [3, 1, 0, 0]


def test_get_67_cents() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2]


def test_get_228_coins() -> None:
    assert get_coin_combination(228) == [3, 0, 0, 9]
