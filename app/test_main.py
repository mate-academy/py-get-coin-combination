import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_returns_expected_result(
    cents: int, expected: list
) -> None:
    assert main.get_coin_combination(cents) == expected


def test_result_uses_nickels_not_only_pennies() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_result_combines_multiple_coin_types() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_zero_cents_returns_no_coins() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_quarters_used_for_large_amounts() -> None:
    assert main.get_coin_combination(50) == [0, 0, 0, 2]
