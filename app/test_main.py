from app.main import get_coin_combination


def test_get_coin_combination_negative() -> None:
    assert get_coin_combination(-1) == [4, 0, 2, -1]


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_one() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_five() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_ten() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_twentyfive() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_fifty() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_big_number() -> None:
    assert get_coin_combination(11111) == [1, 0, 1, 444]
