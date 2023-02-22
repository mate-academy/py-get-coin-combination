from app.main import get_coin_combination


def test_should_return_correct_coin_combination_for_0_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_correct_coin_combination_for_100_cents() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_should_return_correct_coin_combination_for_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_correct_coin_combination_for_6_cent() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_correct_coin_combination_for_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
