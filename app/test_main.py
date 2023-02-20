from app.main import get_coin_combination


def test_combination_with_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_combination_with_6_cent() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_combination_with_17_cent() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_combination_with_50_cent() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_combination_with_0_cent() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
