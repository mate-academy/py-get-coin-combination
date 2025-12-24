from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_with_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_with_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(19) == [4, 1, 1, 0]


def test_with_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_mixed_large_values() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
    assert get_coin_combination(87) == [2, 0, 1, 3]
    assert get_coin_combination(74) == [4, 0, 2, 2]


def test_multiple_of_quarters() -> None:
    assert get_coin_combination(75) == [0, 0, 0, 3]
    assert get_coin_combination(100) == [0, 0, 0, 4]
