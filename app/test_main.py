from app.main import get_coin_combination


def test_should_return_zero_coins_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_penny_for_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickel_for_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_one_dime_for_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_one_quarter_for_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_mixed_coins_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_mixed_coins_for_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_quarters_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
