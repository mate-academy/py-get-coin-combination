from app.main import get_coin_combination


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_ninety_nine_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_one_dollar() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
