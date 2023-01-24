from app.main import get_coin_combination


def test_cents_convert_to_pennies_number() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_cents_convert_to_nickels_number() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_cents_convert_to_dimes_number() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_only_pennies() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_coins_convert_to_the_different_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_coins_convert_to_the_different_types1() -> None:
    assert len(get_coin_combination(41)) == 4
