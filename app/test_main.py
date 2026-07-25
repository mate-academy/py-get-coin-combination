from app.main import get_coin_combination


def test_should_return_correct_combination_for_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_correct_combination_for_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_correct_combination_for_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_correct_combination_for_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_correct_combination_for_41() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
