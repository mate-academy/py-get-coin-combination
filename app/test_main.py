from app.main import get_coin_combination


def test_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickel_and_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_if_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_if_five() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_if_ten() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_if_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_if_25() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_if_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_if_99() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
