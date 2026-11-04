from app.main import get_coin_combination


def test_one_cent_is_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_four_cents_are_four_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]
