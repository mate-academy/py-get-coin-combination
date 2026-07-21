from app.main import get_coin_combination


def test_returns_list() -> None:
    assert type(get_coin_combination(1)) is list


def test_zero_empty_list() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_coin_combinations() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(33) == [3, 1, 0, 1]
