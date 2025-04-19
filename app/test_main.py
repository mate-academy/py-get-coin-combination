from app.main import get_coin_combination


def test_return_zeros_for_zero_input() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_1_for_1_input() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_correct_for_6_input() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_correct_for_17_input() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_correct_for_50_input() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
