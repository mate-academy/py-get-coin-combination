from app.main import get_coin_combination


def test_with_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_with_five_cent() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_with_ten_cent() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_with_twenty_five_cent() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
