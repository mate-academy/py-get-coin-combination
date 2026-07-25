from app.main import get_coin_combination


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickel_and_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_combination_with_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
