from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_just_below_quarter() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_just_above_quarter() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
