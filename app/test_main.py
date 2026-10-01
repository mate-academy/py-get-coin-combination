from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_four_cents() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_nine_cents() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_twenty_four_cents() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
