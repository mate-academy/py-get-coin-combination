from app.main import get_coin_combination


def test_should_return_1penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1penny_and_1nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_2pennies_1nickel_1dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_2quarters4() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
