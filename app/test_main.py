from app.main import get_coin_combination


def test_should_return_list() -> None:
    assert isinstance(get_coin_combination(32), list) is True


def test_value_equal_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_len_equal_four() -> None:
    assert len(get_coin_combination(5)) == 4


def test_fist_stage() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_second_stage() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_third_stage() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_fourth_stage() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_take_big_value() -> None:
    assert get_coin_combination(263) == [3, 0, 1, 10]
