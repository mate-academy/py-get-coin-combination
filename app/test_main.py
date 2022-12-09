import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (4, [4, 0, 0, 0])
    ]
)
def test_only_pennies_values(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"If you have < 5 cents, result should count only {cents} pennies."


@pytest.mark.parametrize(
    "cents, result",
    [
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ]
)
def test_only_dimes_values(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"If you have {cents} cents, result should count only quarters."


@pytest.mark.parametrize(
    "cents, result",
    [
        (123, [3, 0, 2, 4]),
        (211, [1, 0, 1, 8]),
        (577, [2, 0, 0, 23]),
        (884, [4, 1, 0, 35])
    ]
)
def test_zero_values(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"If you have {cents} cents, result should be {result}."


def test_only_dimes_value() -> None:
    assert (
            get_coin_combination(10) == [0, 0, 1, 0]
    ), "If you have 10 cents, result should count only 1 dimes."


def test_only_zero_value() -> None:
    assert (
            get_coin_combination(0) == [0, 0, 0, 0]
    ), "If you have zero cents, result should be list with zero values"


def test_only_nickels_values() -> None:
    assert (
        get_coin_combination(5) == [0, 1, 0, 0]
    ), "If you have 5 cents, result should count only 1 nickels."
