from app.main import get_coin_combination


def test_if_amount_is_one() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_if_amount_is_six() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_if_amount_is_seventeenth() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_if_amount_is_fifty() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
