from app.main import get_coin_combination


def test_have_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_have_6_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_have_17_penny() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_have_50_penny() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
