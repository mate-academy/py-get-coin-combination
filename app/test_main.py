from app.main import get_coin_combination


def test_for_1_cent_return_1_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_for_4_cent_return_4_penny() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_for_5_cent_return_1_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_for_9_cent_return_4_cents_1_nickel() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_for_10_cent_return_1_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_for_19_cent_return_4_cents_1_nickel_1_dime() -> None:
    assert get_coin_combination(19) == [4, 1, 1, 0]


def test_for_25_cent_return_1_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_for_random_cent_return_valid_list() -> None:
    assert get_coin_combination(37) == [2, 0, 1, 1]
    assert get_coin_combination(84) == [4, 1, 0, 3]
    assert get_coin_combination(92) == [2, 1, 1, 3]
    assert get_coin_combination(116) == [1, 1, 1, 4]
    assert get_coin_combination(354) == [4, 0, 0, 14]
    assert get_coin_combination(1488) == [3, 0, 1, 59]

