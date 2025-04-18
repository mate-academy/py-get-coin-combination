from app.main import get_coin_combination


def test_zero_value() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_return_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_return_all_different_by_one() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_return_all_different() -> None:
    assert get_coin_combination(141) == [1, 1, 1, 5]
