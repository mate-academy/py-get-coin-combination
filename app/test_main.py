from app import main
from pytest import mark


def test_zero_amount() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


@mark.parametrize(
    "amount, expected",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
    ],
)
def test_only_pennies(amount: int, expected: list) -> None:
    assert main.get_coin_combination(amount) == expected


@mark.parametrize(
    "amount, expected",
    [
        (5, [0, 1, 0, 0]),
    ],
)
def test_only_nickels(amount: int, expected: list) -> None:
    assert main.get_coin_combination(amount) == expected


@mark.parametrize(
    "amount, expected",
    [
        (10, [0, 0, 1, 0]),
        (20, [0, 0, 2, 0]),
    ],
)
def test_only_dimes(amount: int, expected: list) -> None:
    assert main.get_coin_combination(amount) == expected


@mark.parametrize(
    "amount, expected",
    [
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_only_quarters(amount: int, expected: list) -> None:
    assert main.get_coin_combination(amount) == expected


@mark.parametrize(
    "amount, expected",
    [
        (9, [4, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (30, [0, 1, 0, 1]),
        (31, [1, 1, 0, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_mixed_coin_combinations(amount: int, expected: list) -> None:
    assert main.get_coin_combination(amount) == expected
