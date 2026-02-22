from app.main import get_coin_combination


def test_should_return_correct_combination_for_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_correct_combination_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_correct_combination_for_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_correct_combination_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_zeros_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_handle_large_amount_optimally() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
