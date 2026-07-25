from app.main import get_coin_combination


def test_0_coin() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_4_coin() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_5_coin() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_9_coin() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_10_coin() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_14_coin() -> None:
    assert get_coin_combination(14) == [4, 0, 1, 0]


def test_15_coin() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_24_coin() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_25_coin() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_29_coin() -> None:
    assert get_coin_combination(29) == [4, 0, 0, 1]


def test_30_coin() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]


def test_35_coin() -> None:
    assert get_coin_combination(35) == [0, 0, 1, 1]
