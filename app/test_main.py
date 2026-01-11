from app.main import get_coin_combination


def test_all_zero() -> None:
    cents = 0
    result = get_coin_combination(cents)
    assert result == [0, 0, 0, 0]


def test_50_cents() -> None:
    cents = 50
    result = get_coin_combination(cents)
    assert result == [0, 0, 0, 2]


def test_17_cents() -> None:
    cents = 17
    result = get_coin_combination(cents)
    assert result == [2, 1, 1, 0]
