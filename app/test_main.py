from app.main import get_coin_combination


def test_return_only_pennies() -> None:
    assert get_coin_combination(40) == [0, 1, 1, 1]


def test_return_different_types() -> None:
    assert get_coin_combination(90) == [0, 1, 1, 3]
