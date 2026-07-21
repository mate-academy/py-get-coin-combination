from app.main import get_coin_combination


def test_check_value_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_check_value_5() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_check_value_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_check_value_10() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_check_value_25() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination() -> None:
    assert get_coin_combination(174) == [4, 0, 2, 6]
