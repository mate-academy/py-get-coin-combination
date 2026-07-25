from app.main import get_coin_combination


def test_should_return_1_penny_for_1_cents() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_penny_for_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_2_pennies_1_nickel_1_dime_for_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_2_quarters_for_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
