from app.main import get_coin_combination


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_penny_nickel_and_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_exactly_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_exactly_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_large_amount() -> None:
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_large_amount_with_nickels() -> None:
    assert get_coin_combination(142) == [2, 1, 1, 5]


def test_edge_boundary_just_above_quarter() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]


def test_edge_boundary_just_below_quarter() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_large_cents() -> None:
    assert get_coin_combination(1000) == [0, 0, 0, 40]


def test_large_random_value() -> None:
    assert get_coin_combination(999) == [4, 0, 2, 39]
