from app.main import get_coin_combination


def test_should_return_only_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_penny_and_nickel_and_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_all_values() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
