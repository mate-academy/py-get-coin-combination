from app.main import get_coin_combination


def test_should_return_list() -> None:
    assert isinstance(get_coin_combination(1), list) is True


def test_len_of_return_list_should_eq_4() -> None:
    assert len(get_coin_combination(1)) == 4


def test_math_logic() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_zero_value() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
