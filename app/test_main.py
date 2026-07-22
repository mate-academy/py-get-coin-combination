from app.main import get_coin_combination


def test_coin_combination_when_penny_is_only_one() -> None:
    cents = 1
    actually = get_coin_combination(cents)
    expected = [1, 0, 0, 0]
    assert actually == expected


def test_coin_combination_when_penny_is_6() -> None:
    cents = 6
    actually = get_coin_combination(cents)
    expected = [1, 1, 0, 0]
    assert actually == expected


def test_coin_combination_when_penny_is_17() -> None:
    cents = 17
    actually = get_coin_combination(cents)
    expected = [2, 1, 1, 0]
    assert actually == expected


def test_coin_combination_when_penny_is_50() -> None:
    cents = 50
    actually = get_coin_combination(cents)
    expected = [0, 0, 0, 2]
    assert actually == expected
