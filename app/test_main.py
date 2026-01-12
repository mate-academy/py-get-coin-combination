from app.main import get_coin_combination


def test_should_return_list_with_zero_if_value_is_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_1_penny_if_value_is_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_piece_of_all_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
