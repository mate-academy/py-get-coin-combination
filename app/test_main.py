from app.main import get_coin_combination


def check_when_input_coins_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def check_when_input_large_amount_of_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_returns_correct_result() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
