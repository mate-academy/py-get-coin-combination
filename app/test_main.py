from app.main import get_coin_combination


import pytest


def test_zero_cents_returns_all_zeros() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),  # penny
        (5, [0, 1, 0, 0]),  # nickel
        (10, [0, 0, 1, 0]),  # dime
        (25, [0, 0, 0, 1]),  # quarter
    ],
)
def test_exact_single_coin_combinations(
    cents: int,
    result: list[int],
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents,result",
    [
        (6, [1, 1, 0, 0]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
    ],
)
def test_simple_mixed_combinations(
    cents: int,
    result: list[int],
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents,result",
    [
        (99, [4, 0, 2, 3]),
        (1_000, [0, 0, 0, 40]),
    ],
)
def test_complex_combination_of_all_coins(
    cents: int,
    result: list[int],
) -> None:
    assert get_coin_combination(cents) == result
