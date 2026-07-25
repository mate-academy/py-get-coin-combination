from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cent_one_penny_one_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_thirty_six_cent_two_penny_one_dime_one_quarter() -> None:
    assert get_coin_combination(37) == [2, 0, 1, 1]


def test_fifty_cent_two_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
