from app.main import get_coin_combination


def test_get_coins_when_poins_equal_1() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test_get_coins_when_poins_equal_6() -> None:
    result = get_coin_combination(6)
    assert result == [1, 1, 0, 0]


def test_get_coins_when_poins_equal_16() -> None:
    result = get_coin_combination(16)
    assert result == [1, 1, 1, 0]


def test_get_coins_when_poins_equal_41() -> None:
    result = get_coin_combination(41)
    assert result == [1, 1, 1, 1]


def test_get_coins_when_poins_equal_50() -> None:
    result = get_coin_combination(50)
    assert result == [0, 0, 0, 2]


def test_get_coins_when_poins_equal_100() -> None:
    result = get_coin_combination(100)
    assert result == [0, 0, 0, 4]
