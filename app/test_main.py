from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_multiple_coin_types() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_maximum_combination() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_single_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_single_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_single_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_complex_combination() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2]
