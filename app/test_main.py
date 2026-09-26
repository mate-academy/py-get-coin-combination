from app.main import get_coin_combination


def test_get_zero_coin() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_one_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_five_coin() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_six_coin() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_seventeen_coin() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_fifty_coin() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_max_coin() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_forty_coin() -> None:
    assert get_coin_combination(40) == [0, 1, 1, 1]


def test_more_one_hundred_coins() -> None:
    assert get_coin_combination(137) == [2, 0, 1, 5]
