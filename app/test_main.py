from app.main import get_coin_combination


def test_zero_coins() -> None:
    cents = get_coin_combination(0)
    assert cents == [0, 0, 0, 0]


def test_penny() -> None:
    cents = get_coin_combination(1)
    assert cents == [1, 0, 0, 0]


def test_nickel() -> None:
    cents = get_coin_combination(5)
    assert cents == [0, 1, 0, 0]


def test_dime() -> None:
    cents = get_coin_combination(20)
    assert cents == [0, 0, 2, 0]


def test_quarter() -> None:
    cents = get_coin_combination(75)
    assert cents == [0, 0, 0, 3]


def test_all_coins_type() -> None:
    cents = get_coin_combination(67)
    assert cents == [2, 1, 1, 2]
