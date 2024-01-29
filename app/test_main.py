from app.main import get_coin_combination


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_multiple_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_multiple_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_value() -> None:
    assert get_coin_combination(99) == [4, 1, 2, 3]
