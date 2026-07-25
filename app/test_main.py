from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(2) == [2, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_on_one_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_one_nominal() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]
