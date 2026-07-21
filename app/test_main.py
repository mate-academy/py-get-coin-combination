from app.main import get_coin_combination


def test_should_return_zero_when_no_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_count_cents() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_count_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_count_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_count_quarters() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
