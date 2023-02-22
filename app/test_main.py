from app.main import get_coin_combination


def test_coin_combination_for_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_coin_combination_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_coin_combination_for_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_coin_combination_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_coin_combination_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_coin_combination_for_large_value() -> None:
    assert get_coin_combination(243) == [3, 1, 1, 9]


def test_coin_combination_for_negative_value() -> None:
    assert not get_coin_combination(-5)
