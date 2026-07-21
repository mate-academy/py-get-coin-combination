from app.main import get_coin_combination


def test_first_emae() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_second_emae() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_third_emae() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fourth_emae() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
