from app.main import get_coin_combination


def test_return_not_only_pennies() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_return_only_one_type() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
