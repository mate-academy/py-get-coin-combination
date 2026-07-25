from app.main import get_coin_combination


def test_coin_is_0() -> None:
    coins = get_coin_combination(0)
    assert coins == [0, 0, 0, 0]


def test_coin_is_1() -> None:
    coins = get_coin_combination(1)
    assert coins == [1, 0, 0, 0]


def test_coin_is_6() -> None:
    coins = get_coin_combination(6)
    assert coins == [1, 1, 0, 0]


def test_coin_is_17() -> None:
    coins = get_coin_combination(17)
    assert coins == [2, 1, 1, 0]


def test_coin_is_42() -> None:
    coins = get_coin_combination(42)
    assert coins == [2, 1, 1, 1]


def test_coin_is_50() -> None:
    coins = get_coin_combination(50)
    assert coins == [0, 0, 0, 2]


def test_coin_is_632() -> None:
    coins = get_coin_combination(632)
    assert coins == [2, 1, 0, 25]
