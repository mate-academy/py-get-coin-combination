from app.main import get_coin_combination


def test_zero_cents_should_return_all_zeros() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_pennies_only() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_dimes_combination() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_nickels_combination() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_quarters_combination() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_complex_combination() -> None:
    assert get_coin_combination(43) == [3, 1, 1, 1]

    assert get_coin_combination(99) == [4, 0, 2, 3]
