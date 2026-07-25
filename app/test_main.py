from app.main import get_coin_combination


def test_reverse_conversion_should_be_equal_to_cent() -> None:
    pennies = get_coin_combination(10)[0]
    nickels = get_coin_combination(10)[1] * 5
    dimes = get_coin_combination(10)[2] * 10
    quarters = get_coin_combination(10)[3] * 25
    assert pennies + nickels + dimes + quarters == 10


def test_should_issue_any_coins() -> None:
    assert get_coin_combination(12) == [2, 0, 1, 0]
    assert get_coin_combination(31) == [1, 1, 0, 1]
