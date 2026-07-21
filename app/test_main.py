from app.main import get_coin_combination


def test_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], "test 1"


def test_2() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0], "test 2"


def test_3() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0], "test 3"


def test_4() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2], "test 4"
