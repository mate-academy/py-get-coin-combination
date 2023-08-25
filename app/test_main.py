from app.main import get_coin_combination


def test_can_add_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_can_add_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_can_add_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_can_add_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_list_of_zero_if_input_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_can_add_different_set_of_all_coins() -> None:
    assert get_coin_combination(42) == [2, 1, 1, 1]
