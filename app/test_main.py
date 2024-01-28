from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickles() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_penny_and_nickles_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cent() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_big_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
