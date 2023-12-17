from app.main import get_coin_combination


def test_when_func_takes_value_less_than_5() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_when_func_takes_value_equal_5() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_when_func_takes_value_equal_10() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_when_func_takes_value_equal_25() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_when_func_returns_different_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
