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


def test_thirty_cents() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]


def test_sixty_cents() -> None:
    assert get_coin_combination(60) == [0, 0, 1, 2]


def test_one_hundred_cents() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_large_number() -> None:
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_with_extra_penny() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
