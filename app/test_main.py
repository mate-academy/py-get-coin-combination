from app.main import get_coin_combination


def test_get_coin_combination_check_penny() -> None:
    assert get_coin_combination(1)[0] == 1


def test_get_coin_combination_check_nickel() -> None:
    assert get_coin_combination(5)[1] == 1


def test_get_coin_combination_check_dime() -> None:
    assert get_coin_combination(10)[2] == 1


def test_get_coin_combination_check_quarters() -> None:
    assert get_coin_combination(25)[3] == 1


def test_get_coin_combination_check_all() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
