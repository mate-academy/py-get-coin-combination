from app.main import get_coin_combination


def test_should_return_2_pennies_1_nickel_1_dime_2_quarters() -> None:
    assert get_coin_combination(69) == [4, 1, 1, 2]
