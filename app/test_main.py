from app.main import get_coin_combination


def test_minimal_value() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_one_coin_value() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_six_coins_value() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_seventeen_coins_value() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_fifty_coins_value() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_ninety_nine_coins_value() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
