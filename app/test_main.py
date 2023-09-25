from app.main import get_coin_combination


def test_return_only_pennies() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
