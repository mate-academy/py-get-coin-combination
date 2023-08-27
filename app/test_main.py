from app.main import get_coin_combination


def test_should_return_four_penny() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_one_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_every_type_of_coin() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
