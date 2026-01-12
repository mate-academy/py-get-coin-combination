from app.main import get_coin_combination


def test_normal_function_operation() -> None:
    assert get_coin_combination(73) == [3, 0, 2, 2]


def test_cents_is_zero_return_list_of_zeros() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
