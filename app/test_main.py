from app.main import get_coin_combination


def test_for_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_for_one_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_for_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_for_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_for_each_other() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_for_penny_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_for__penny_nickel_dime() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_for_penny_quarter() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
