from app.main import get_coin_combination


def test_should_return_no_coins_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_only_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_only_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
