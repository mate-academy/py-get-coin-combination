from app.main import get_coin_combination


def test_should_be_only_cents() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_be_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_be_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_all_the_coins_should_be_there() -> None:
    assert get_coin_combination(66) == [1, 1, 1, 2]
