from app.main import get_coin_combination


def test_should_return_1_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_1_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_1_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_all() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
