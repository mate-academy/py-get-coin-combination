from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(2) == [2, 0, 0, 0]
    assert get_coin_combination(3) == [3, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_return_only_one_type() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(75) == [0, 0, 0, 3]
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_mixed_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]
