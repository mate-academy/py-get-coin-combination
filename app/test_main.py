from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_thirty_one_cents() -> None:
    assert get_coin_combination(31) == [1, 1, 0, 1]  # Помилковий результат


def test_ninety_nine_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]  # Помилковий результат


def test_large_amount() -> None:
    assert get_coin_combination(157) == [2, 1, 0, 6]


def test_example_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_example_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
