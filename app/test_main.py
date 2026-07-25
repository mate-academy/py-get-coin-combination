from app.main import get_coin_combination


def test_get_coin_combination_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
