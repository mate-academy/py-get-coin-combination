from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(30) == [0, 1, 0, 1]


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_boundary_conditions() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]
