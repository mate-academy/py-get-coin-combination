from app.main import get_coin_combination


def test_should_return_pennies_nickel_dime_if_cents_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_quarter_when_cents_is_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
