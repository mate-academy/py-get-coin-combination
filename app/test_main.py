from app.main import get_coin_combination


def test_should_return_int() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_should_return_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_mixed_combination() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_zero_for_zero_cents() -> None :
    assert get_coin_combination(0) == [0, 0, 0, 0]
