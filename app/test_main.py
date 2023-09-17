from app.main import get_coin_combination


def test_no_coin() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_all_one_in_result() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
