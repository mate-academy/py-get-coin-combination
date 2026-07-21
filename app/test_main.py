from app.main import get_coin_combination


def test_if_number_of_coins_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_if_only_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_if_six_cents_needed() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_if_seventeen_cents_needed() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_if_fifty_cents_needed() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
