from app.main import get_coin_combination


def test_get_coin_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_nickel_and_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_dime_nickel_penny() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_two_quaters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
